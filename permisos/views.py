from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .decorators import user_is_admin, user_is_admin_or_personal_administrativo
from django import forms
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from weasyprint import HTML
import os

from .forms import (
    UserRegisterForm,
    UserPermissionRequestForm,
    AdminPermissionForm,
    AdminPermissionRequestForm,
    CompensationRequestForm,
    UserProfileForm,
)
from .models import (
    PermissionRequest,
    PermissionRequestAdmin,
    CompensationRequest,
    UserProfile,
)

@login_required
def home(request):
    return render(request, "home.html")


# ----------------------------
# Autenticación
# ----------------------------


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm(),
                    "error": "El nombre de usuario o contraseña es incorrecto.",
                },
            )

        if user is not None and not user.is_active:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm(),
                    "error": "Tu cuenta está inactiva. Contacta al administrador.",
                },
            )

        else:
            login(request, user)
            profile, created = UserProfile.objects.get_or_create(user=user)
            if not profile.full_name or not profile.rut or not profile.firma:
                return redirect("complete_profile")
            return redirect("home")


@login_required
def signout(request):
    logout(request)
    messages.info(request, "Haz cerrado sesión.")
    return redirect("signin")


# ----------------------------
# Perfil de usuario y gestión
# ----------------------------


@login_required
def complete_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if profile.full_name and profile.rut and profile.firma:
        return redirect("home")

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil completado exitosamente.")
            return redirect("home")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "complete_profile.html", {"form": form})



@login_required
#@user_is_admin
def user_management(request):
    # Consulta todos los perfiles y usuarios relacionados
    users = UserProfile.objects.select_related("user").all()

    # Asegurarse de manejar valores nulos o vacíos
    for user in users:
        if not user.position:
            user.position = "No especificado"
        if not user.establishment:
            user.establishment = "No especificado"
        if not user.permissions:
            user.permissions = "No asignado"

    return render(request, "user_management.html", {"users": users})

@login_required
#@user_is_admin
def create_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Usuario {user.username} creado exitosamente.")
            return redirect("user_management")
        else:
            return render(request, "create_user.html", {"form": form, "error": "Error en el formulario."})
    else:
        form = UserRegisterForm()
    return render(request, "create_user.html", {"form": form})


@login_required
#@user_is_admin
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user_management")
    else:
        form = UserRegisterForm(instance=user)
    return render(request, "edit_user.html", {"form": form})


@login_required
#@user_is_admin
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("user_management")
    return render(request, "delete_user.html", {"user": user})


@login_required
#@user_is_admin
def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Usuario {user.username} creado exitosamente.")
            return redirect("user_management")
        else:
            return render(request, "register.html", {"form": form, "error": "Error en el formulario."})
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


@login_required
def user_permission_status(request, tipo=None):
    permissions = []

    if tipo == "FERIADO":
        permissions = PermissionRequest.objects.filter(user=request.user, request_type="FERIADO")
    elif tipo == "ADMINISTRATIVO":
        # Añadimos `request_type` manualmente para uniformidad
        permissions = PermissionRequestAdmin.objects.filter(user=request.user).values(
            "id", "full_name", "rut", "date_from", "date_to", "estado"
        )
        for permission in permissions:
            permission["request_type"] = "ADMINISTRATIVO"
    elif tipo == "COMPENSACION":
        # Añadimos `request_type` manualmente para uniformidad
        permissions = CompensationRequest.objects.filter(user=request.user).values(
            "id", "full_name", "rut", "date_from", "date_to", "estado"
        )
        for permission in permissions:
            permission["request_type"] = "COMPENSACION"
    else:
        permissions = PermissionRequest.objects.filter(user=request.user)

    return render(
        request,
        "user_permission_status.html",
        {"permissions": permissions, "tipo": tipo},
    )



# ----------------------------
# Solicitudes de permisos
# ----------------------------


@login_required
def request_permission(request):
    if request.method == "POST":
        form = UserPermissionRequestForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            permission_request = form.save(commit=False)
            permission_request.user = request.user
            permission_request.save()
            messages.success(request, "Su solicitud ha sido enviada exitosamente.")
            return redirect("home")
    else:
        form = UserPermissionRequestForm(user=request.user)
    return render(request, "request_permission.html", {"form": form})


@login_required
def admin_permission_request(request):
    if request.method == "POST":
        form = AdminPermissionRequestForm(
            request.POST, request.FILES, user=request.user
        )
        if form.is_valid():
            permission_request = form.save(commit=False)
            permission_request.user = request.user
            permission_request.save()
            messages.success(request, "Solicitud enviada exitosamente.")
            return redirect("home")
    else:
        form = AdminPermissionRequestForm(user=request.user)
    return render(request, "admin_permission_request.html", {"form": form})


@login_required
def compensation_request(request):
    if request.method == "POST":
        form = CompensationRequestForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            compensation_request = form.save(commit=False)
            compensation_request.user = request.user
            compensation_request.save()
            messages.success(request, "Solicitud enviada exitosamente.")
            return redirect("home")
    else:
        form = CompensationRequestForm(user=request.user)
    return render(request, "compensation_request.html", {"form": form})


# ----------------------------
# Listados y detalles de permisos
# ----------------------------
@login_required
def list_permissions(request, model, template_name, query_param="q"):
    query = request.GET.get(query_param, "")
    permissions = model.objects.filter(
        Q(full_name__icontains=query) | Q(rut__icontains=query)
    )
    return render(request, template_name, {"permissions": permissions, "query": query})


@login_required
#@user_is_admin_or_personal_administrativo
def regular_permission_list(request):
    query = request.GET.get("q", "")
    regular_permissions = PermissionRequest.objects.filter(
        Q(full_name__icontains=query) | Q(rut__icontains=query)
    )
    return render(
        request,
        "regular_permission_list.html",
        {"regular_permissions": regular_permissions, "query": query},
    )



@login_required
#@user_is_admin_or_personal_administrativo
def admin_permission_list(request):
    query = request.GET.get("q", "")
    admin_permissions = PermissionRequestAdmin.objects.filter(
        Q(full_name__icontains=query) | Q(rut__icontains=query)
    )
    return render(
        request,
        "admin_permission_list.html",
        {"admin_permissions": admin_permissions, "query": query},
    )


@login_required
#@user_is_admin_or_personal_administrativo
def compensation_request_list(request):
    query = request.GET.get("q", "")
    compensation_requests = CompensationRequest.objects.filter(
        Q(full_name__icontains=query) | Q(rut__icontains=query)
    )
    return render(
        request,
        "compensation_request_list.html",
        {"compensation_requests": compensation_requests, "query": query},
    )





@login_required
#@user_is_admin_or_personal_administrativo
def regular_permission_detail(request, permission_id):
    permission = get_object_or_404(PermissionRequest, id=permission_id)
    if request.method == "POST":
        form = AdminPermissionForm(request.POST, request.FILES, instance=permission)
        if form.is_valid():
            estado = request.POST.get("estado")
            if estado in ["autorizado", "no_autorizado", "pendiente"]:
                permission.estado = estado
            form.save()
            messages.success(request, f"Permiso actualizado a {estado}.")
            return redirect("regular_permission_list")
    else:
        form = AdminPermissionForm(instance=permission)
    return render(
        request,
        "regular_permission_detail.html",
        {"form": form, "permission": permission},
    )


@login_required
#@user_is_admin_or_personal_administrativo
def admin_permission_detail(request, permission_id):
    permission = get_object_or_404(PermissionRequestAdmin, id=permission_id)
    if request.method == "POST":
        form = AdminPermissionForm(request.POST, request.FILES, instance=permission)
        if form.is_valid():
            permission = form.save(commit=False)
            # Guardar campos adicionales
            permission.estado = request.POST.get("estado")
            permission.date_from = form.cleaned_data.get("date_from")
            permission.date_to = form.cleaned_data.get("date_to")
            permission.firma_funcionario = form.cleaned_data.get("firma_funcionario")
            permission.save()
            messages.success(request, "Solicitud actualizada correctamente.")
            return redirect("admin_permission_list")
    else:
        form = AdminPermissionForm(instance=permission)

    return render(
        request,
        "admin_permission_detail.html",
        {"form": form, "permission": permission},
    )


@login_required
#@user_is_admin_or_personal_administrativo
def admin_permission_admin_detail(request, permission_id):
    permission = get_object_or_404(PermissionRequestAdmin, id=permission_id)
    if request.method == "POST":
        form = AdminPermissionForm(request.POST, request.FILES, instance=permission)
        if form.is_valid():
            estado = request.POST.get("estado")
            if estado in ["autorizado", "no_autorizado", "pendiente"]:
                permission.estado = estado
            form.save()
            messages.success(
                request, f"La solicitud administrativa ha sido actualizada a {estado}."
            )
            return redirect("admin_permission_list")
    else:
        form = AdminPermissionForm(instance=permission)
    return render(
        request,
        "admin_permission_admin_detail.html",
        {"form": form, "permission": permission},
    )


@login_required
#@user_is_admin_or_personal_administrativo
def compensation_request_detail(request, request_id):
    compensation_request = get_object_or_404(CompensationRequest, id=request_id)
    if request.method == "POST":
        form = AdminPermissionForm(
            request.POST, request.FILES, instance=compensation_request
        )
        if form.is_valid():
            estado = request.POST.get("estado")
            if estado in ["autorizado", "no_autorizado", "pendiente"]:
                compensation_request.estado = estado
            form.save()
            messages.success(
                request, f"La solicitud de compensación ha sido actualizada a {estado}."
            )
            return redirect("compensation_request_list")
    else:
        form = AdminPermissionForm(instance=compensation_request)
    return render(
        request,
        "compensation_request_detail.html",
        {"form": form, "compensation_request": compensation_request},
    )


# ----------------------------
# Generación de PDFs
# ----------------------------


@login_required
def generate_user_permission_pdf(request, permission_id):
    try:
        # Obtén el permiso asociado
        permission = get_object_or_404(
            PermissionRequest, id=permission_id, user=request.user
        )

        # Renderizar el PDF sin restricciones de estado
        return _generate_pdf(
            template_name="permission_pdf_template.html",
            context={
                "permission": permission,
                "full_name": permission.full_name,
                "rut": permission.rut,
                "position": permission.position,
                "establishment": permission.establishment,
                "date_from": permission.date_from,
                "date_to": permission.date_to,
                "estado": permission.estado,
                "firma_funcionario": permission.firma_funcionario,
            },
            filename=f"Solicitud_Feriado_{permission_id}.pdf",
        )

    except PermissionRequest.DoesNotExist:
        messages.error(request, "El permiso solicitado no existe.")
        return redirect("user_permission_status_feriado")

    except Exception as e:
        messages.error(request, f"Error inesperado al generar el PDF: {str(e)}")
        return redirect("user_permission_status_feriado")


@login_required
def generate_admin_permission_pdf(request, permission_id):
    try:
        # Obtén el permiso administrativo asociado
        permission = get_object_or_404(
            PermissionRequestAdmin, id=permission_id, user=request.user
        )

        # Renderizar el PDF sin restricciones de estado
        return _generate_pdf(
            template_name="admin_permission_pdf_template.html",
            context={
                "permission": permission,
                "full_name": permission.full_name,
                "rut": permission.rut,
                "position": permission.position,
                "establishment": permission.establishment,
                "date_from": permission.date_from,
                "date_to": permission.date_to,
                "estado": permission.estado,
                "firma_funcionario": permission.firma_funcionario,
            },
            filename=f"Permiso_Admin_{permission_id}.pdf",
        )

    except PermissionRequestAdmin.DoesNotExist:
        messages.error(request, "El permiso administrativo solicitado no existe.")
        return redirect("user_permission_status_administrativo")

    except Exception as e:
        messages.error(request, f"Error inesperado al generar el PDF: {str(e)}")
        return redirect("user_permission_status_administrativo")


@login_required
def generate_compensation_request_pdf(request, request_id):
    try:
        # Obtén la solicitud de compensación asociada
        compensation_request = get_object_or_404(
            CompensationRequest, id=request_id, user=request.user
        )

        # Renderizar el PDF sin restricciones de estado
        return _generate_pdf(
            template_name="compensation_pdf_template.html",
            context={
                "compensation_request": compensation_request,
                "full_name": compensation_request.full_name,
                "rut": compensation_request.rut,
                "position": compensation_request.position,
                "establishment": compensation_request.establishment,
                "date_from": compensation_request.date_from,
                "date_to": compensation_request.date_to,
                "time_from": compensation_request.time_from,
                "time_to": compensation_request.time_to,
                "estado": compensation_request.estado,
                "firma_funcionario": compensation_request.firma_funcionario,
            },
            filename=f"Compensacion_{request_id}.pdf",
        )

    except CompensationRequest.DoesNotExist:
        messages.error(request, "La solicitud de compensación no existe.")
        return redirect("user_permission_status_compensacion")

    except Exception as e:
        messages.error(request, f"Error inesperado al generar el PDF: {str(e)}")
        return redirect("user_permission_status_compensacion")


def _generate_pdf(template_name, context, filename):
    try:
        # Renderizar el contenido del PDF
        html_string = render_to_string(template_name, context)

        # Directorio temporal para el archivo PDF
        temp_dir = os.path.join(os.path.dirname(__file__), "temp_files")
        os.makedirs(temp_dir, exist_ok=True)
        temp_pdf_path = os.path.join(temp_dir, filename)

        # Eliminar archivo existente si ya está presente
        if os.path.isfile(temp_pdf_path):
            os.remove(temp_pdf_path)

        # Generar el PDF
        HTML(string=html_string).write_pdf(temp_pdf_path)
        with open(temp_pdf_path, "rb") as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="{filename}"'
            return response

    except Exception as e:
        raise RuntimeError(f"Error al generar el PDF: {str(e)}")

@login_required
#@user_is_admin_or_personal_administrativo
def approve_reject_request(request, request_id):
    """
    Vista para que los administradores aprueben o rechacen solicitudes.
    """
    compensation_request = get_object_or_404(CompensationRequest, id=request_id)

    if request.method == "POST":
        form = AdminPermissionForm(request.POST, instance=compensation_request)
        if form.is_valid():
            compensation_request = form.save(commit=False)
            estado = request.POST.get("estado")
            if estado in ["aprobado", "rechazado", "pendiente"]:
                compensation_request.estado = estado
            compensation_request.save()
            messages.success(request, f"La solicitud ha sido actualizada a {estado}.")
            return redirect("compensation_request_list")
    else:
        form = AdminPermissionForm(instance=compensation_request)

    return render(
        request,
        "approve_reject_request.html",
        {"form": form, "compensation_request": compensation_request},
    )
