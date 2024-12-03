from django.urls import path
from permisos import views

urlpatterns = [
    # Autenticación y navegación
    path('', views.signin, name='signin'),  # Página de inicio
    path('signup/', views.signup, name='signup'),  # Registro de usuario
    path('signin/', views.signin, name='signin'),  # Inicio de sesión
    path('signout/', views.signout, name='signout'),  # Cierre de sesión
    path('home/', views.home, name='home'),  # Página principal para usuarios autenticados

    # Gestión de usuarios (solo para administradores)
    path('user-management/', views.user_management, name='user_management'),  # Listado de usuarios
    path('user-management/create/', views.create_user, name='create_user'),  # Crear usuario
    path('user-management/edit/<int:user_id>/', views.edit_user, name='edit_user'),  # Editar usuario
    path('user-management/delete/<int:user_id>/', views.delete_user, name='delete_user'),  # Eliminar usuario

    # Listados de permisos
    path('regular-permissions/', views.regular_permission_list, name='regular_permission_list'),  # Listado de solicitudes de feriado legal
    path('admin-permissions/', views.admin_permission_list, name='admin_permission_list'),  # Listado de solicitudes de permiso administrativo
    path('compensation-requests/', views.compensation_request_list, name='compensation_request_list'),  # Listado de solicitudes de compensación de tiempo

    # Formularios de solicitud
    path('request-permission/', views.request_permission, name='request_permission'),  # Solicitud de feriado legal
    path('admin-permission-request/', views.admin_permission_request, name='admin_permission_request'),  # Solicitud de permiso administrativo
    path('compensation-request/', views.compensation_request, name='compensation_request'),  # Solicitud de compensación de tiempo

    # Detalles de permisos
    path('permissions/<int:permission_id>/', views.admin_permission_detail, name='admin_permission_detail'),  # Detalle de feriado legal
    path('regular-permissions/<int:permission_id>/', views.regular_permission_detail, name='regular_permission_detail'),  # Detalle de solicitud de feriado legal (usuario normal)
    path('admin-permissions/<int:permission_id>/', views.admin_permission_admin_detail, name='admin_permission_admin_detail'),  # Detalle de permiso administrativo
    path('compensation-requests/<int:request_id>/', views.compensation_request_detail, name='compensation_request_detail'),  # Detalle de compensación de tiempo

    # Estado de solicitudes de permisos con tipo especificado
    path('mis-solicitudes/feriado/', views.user_permission_status, {'tipo': 'FERIADO'}, name='user_permission_status_feriado'),
    path('mis-solicitudes/administrativo/', views.user_permission_status, {'tipo': 'ADMINISTRATIVO'}, name='user_permission_status_administrativo'),
    path('mis-solicitudes/compensacion/', views.user_permission_status, {'tipo': 'COMPENSACION'}, name='user_permission_status_compensacion'),

    # Generación de PDF
    path('generate-user-permission-pdf/<int:permission_id>/', views.generate_user_permission_pdf, name='generate_user_permission_pdf'),  # PDF para usuario normal
    path('generate-admin-permission-pdf/<int:permission_id>/', views.generate_admin_permission_pdf, name='generate_admin_permission_pdf'),  # PDF para permisos administrativos
    path('generate-compensation-request-pdf/<int:request_id>/', views.generate_compensation_request_pdf, name='generate_compensation_request_pdf'),  # PDF para compensación de tiempo

    # Completar perfil
    path('complete-profile/', views.complete_profile, name='complete_profile'),  # Completar perfil del usuario
]
