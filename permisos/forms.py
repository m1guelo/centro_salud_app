from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PermissionRequest, PermissionRequestAdmin, CompensationRequest, UserProfile

# Formulario de Registro de Usuario
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=UserProfile.USER_TYPE_CHOICES,
        label="Tipo de Usuario",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_type = self.cleaned_data['user_type']
            UserProfile.objects.create(user=user, user_type=user_type)
        return user


# Formulario de Solicitud de Permiso (Usuarios Normales)
class UserPermissionRequestForm(forms.ModelForm):
    class Meta:
        model = PermissionRequest
        fields = [
            'full_name', 'rut', 'position', 'establishment',
            'date_from', 'date_to', 'period', 'firma_funcionario',
        ]
        labels = {
            'full_name': 'Nombre completo',
            'rut': 'RUT',
            'position': 'Cargo',
            'establishment': 'Establecimiento',
            'date_from': 'Fecha desde',
            'date_to': 'Fecha hasta',
            'period': 'Periodo',
            'firma_funcionario': 'Firma del funcionario',
        }
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Sacamos el usuario
        super().__init__(*args, **kwargs)
        if user:
            # Autocompletamos los campos con datos del perfil del usuario
            profile = user.userprofile
            self.fields['full_name'].initial = profile.full_name
            self.fields['rut'].initial = profile.rut
            self.fields['position'].initial = profile.position
            self.fields['establishment'].initial = profile.establishment


# Formulario de Gestión de Permisos (Usuarios Administrativos)
class AdminPermissionForm(forms.ModelForm):
    class Meta:
        model = PermissionRequest
        fields = [
            'autorizado', 'anticipado', 'postergado', 
            'additional_date_from', 'additional_date_to', 
            'firma_funcionario'
        ]
        labels = {
            'autorizado': 'Autorizado',
            'anticipado': 'Anticipado',
            'postergado': 'Postergado',
            'additional_date_from': 'Fecha desde',
            'additional_date_to': 'Fecha hasta',
            'firma_funcionario': 'Firma del administrador',
        }
        widgets = {
            'additional_date_from': forms.DateInput(attrs={'type': 'date'}),
            'additional_date_to': forms.DateInput(attrs={'type': 'date'}),
        }

class AdminPermissionRequestForm(forms.ModelForm):
    class Meta:
        model = PermissionRequestAdmin
        fields = [
            "full_name", "rut", "position", "establishment",
            "number_of_days", "date_from", "date_to",
            "jornada", "firma_funcionario",
        ]
        labels = {
            "full_name": "Nombre completo",
            "rut": "RUT",
            "position": "Cargo",
            "establishment": "Establecimiento",
            "number_of_days": "Número de días",
            "date_from": "Fecha desde",
            "date_to": "Fecha hasta",
            "jornada": "Jornada",
            "firma_funcionario": "Firma del funcionario",
        }
        widgets = {
            "date_from": forms.DateInput(attrs={"type": "date"}),
            "date_to": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            profile = user.userprofile
            self.fields["full_name"].initial = profile.full_name
            self.fields["rut"].initial = profile.rut

        
class CompensationRequestForm(forms.ModelForm):
    class Meta:
        model = CompensationRequest
        fields = [
            'full_name', 'rut', 'position', 'establishment',
            'number_of_hours', 'date_from', 'date_to',
            'time_from', 'time_to', 'firma_funcionario'
        ]
        labels = {
            'full_name': 'Nombre completo',
            'rut': 'RUT',
            'position': 'Cargo',
            'establishment': 'Establecimiento',
            'number_of_hours': 'Número de horas',
            'date_from': 'Fecha desde',
            'date_to': 'Fecha hasta',
            'time_from': 'Horario desde',
            'time_to': 'Horario hasta',
            'firma_funcionario': 'Firma del funcionario',
        }
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
            'time_from': forms.TimeInput(attrs={'type': 'time'}),
            'time_to': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extraer usuario
        super().__init__(*args, **kwargs)
        if user:
            # Asignar valores iniciales desde el perfil del usuario
            profile = user.userprofile
            self.fields['full_name'].initial = profile.full_name
            self.fields['rut'].initial = profile.rut
            self.fields['position'].initial = profile.position
            self.fields['establishment'].initial = profile.establishment

        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'rut', 'firma']
        labels = {
            'full_name': 'Nombre completo',
            'rut': 'RUT',
            'firma': 'Firma',
        }
