from django.http import HttpResponseForbidden
from functools import wraps

def user_is_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, "userprofile") and request.user.userprofile.user_type == "admin":
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    return _wrapped_view

def user_is_personal_administrativo(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, "userprofile") and request.user.userprofile.user_type == "personal_administrativo":
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    return _wrapped_view

def user_is_normal(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, "userprofile") and request.user.userprofile.user_type == "usuario_normal":
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    return _wrapped_view

def user_is_admin_or_personal_administrativo(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if (
            hasattr(request.user, "userprofile")
            and request.user.userprofile.user_type in ["admin", "personal_administrativo"]
        ):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    return _wrapped_view
