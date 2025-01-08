from django.core.exceptions import PermissionDenied
from functools import wraps
from permisos import views

# Decorador para usuarios administradores
def user_is_admin(view_func):
    """
    Permite el acceso solo a usuarios con el tipo 'admin'.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, "userprofile") and request.user.userprofile.user_type == "admin":
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("Acceso denegado. Solo para administradores.")
    return _wrapped_view

# Decorador para usuarios normales
def user_is_normal(view_func):
    """
    Permite el acceso solo a usuarios con el tipo 'usuario_normal'.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, "userprofile") and request.user.userprofile.user_type == "usuario_normal":
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("Acceso denegado. Solo para usuarios normales.")
    return _wrapped_view

# Decorador para vistas accesibles por todos los tipos de usuarios
def user_has_access(view_func):
    """
    Permite el acceso a todos los usuarios autenticados (admin y usuarios normales).
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, "userprofile") and request.user.userprofile.user_type in ["admin", "usuario_normal"]:
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("Acceso denegado.")
    return _wrapped_view

# Decorador para vistas accesibles solo por administradores y usuarios normales
def user_is_admin_or_normal(view_func):
    """
    Permite el acceso a usuarios con el tipo 'admin' o 'usuario_normal'.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, "userprofile") and request.user.userprofile.user_type in ["admin", "usuario_normal"]:
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("Acceso denegado. Solo para administradores o usuarios normales.")
    return _wrapped_view
