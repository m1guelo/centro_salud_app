from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # User position and department choices
    CARGO_CHOICES = [
        ('Dentista', 'Dentista'),
        ('Medico', 'Médico'),
        ('Quimico-Farmaceutico', 'Químico-Farmacéutico'),
        ('Asistente Social', 'Asistente Social'),
        ('Enfermera', 'Enfermera'),
        ('Kinesiologo', 'Kinesiólogo'),
        ('Matrona', 'Matrona'),
        ('Nutricionista', 'Nutricionista'),
        ('Psicologo', 'Psicólogo'),
        ('Tecnologo Medico', 'Tecnólogo Médico'),
        ('Fonoaudiologo', 'Fonoaudiólogo'),
        ('Terapeuta Ocupacional', 'Terapeuta Ocupacional'),
        ('Educadora de Parvulos', 'Educadora de Párvulos'),
        ('Profesor de Educacion Fisica', 'Profesor de Educación Física'),
        ('Abogado', 'Abogado'),
        ('Ingeniero en Informatica', 'Ingeniero en Informática'),
        ('Ingeniero en Prevencion de Riesgos', 'Ingeniero en Prevención de Riesgos'),
        ('Ingeniero en Administracion de Empresas', 'Ingeniero en Administración de Empresas'),
        ('Ingeniero Comercial', 'Ingeniero Comercial'),
        ('Contador Auditor', 'Contador Auditor'),
        ('TENS Enfermeria', 'TENS (Enfermería)'),
        ('TANS Administracion', 'TANS (Administración)'),
        ('Podologo', 'Podólogo'),
        ('Estadistico', 'Estadístico'),
        ('Programador', 'Programador/ Técnico en Computación'),
        ('Paramedico', 'Paramédico'),
        ('Secretaria', 'Secretaria'),
        ('Administrativos de Salud', 'Administrativos de Salud'),
        ('Auxiliar de Servicio', 'Auxiliar de Servicio'),
        ('Conductor', 'Conductor'),
        ('Estafeta', 'Estafeta'),
        ('Director de Consultorio', 'Director de Consultorio (CESFAM Arrau Méndez)'),
        ('Director de Departamento de Salud Municipal', 'Director de Departamento de Salud Municipal'),
    ]

    DEPARTAMENTO_CHOICES = [
        ('Posta de Salud Rural Villa Baviera', 'Posta de Salud Rural Villa Baviera'),
        ('Posta de Salud Rural Los Canelos', 'Posta de Salud Rural Los Canelos'),
        ('Posta de Salud Rural Bullileo', 'Posta de Salud Rural Bullileo'),
        ('Posta de Salud Rural Bajos de Huenutil', 'Posta de Salud Rural Bajos de Huenutil'),
        ('Posta de Salud Rural Catillo', 'Posta de Salud Rural Catillo'),
        ('Posta de Salud Rural Digua', 'Posta de Salud Rural Digua'),
        ('Posta de Salud Rural Monte Flor', 'Posta de Salud Rural Monte Flor'),
        ('Posta de Salud Rural San Alejo', 'Posta de Salud Rural San Alejo'),
        ('Posta de Salud Rural Talquita', 'Posta de Salud Rural Talquita'),
        ('Posta de Salud Rural Los Carros', 'Posta de Salud Rural Los Carros'),
        ('Posta de Salud Rural Perquilauquén', 'Posta de Salud Rural Perquilauquén'),
        ('Posta de Salud Rural La Orilla', 'Posta de Salud Rural La Orilla'),
        ('Posta de Salud Rural Fuerte Viejo', 'Posta de Salud Rural Fuerte Viejo'),
        ('Centro Comunitario de Salud Familiar Los Olivos', 'Centro Comunitario de Salud Familiar Los Olivos'),
        ('Centro de Salud Familiar Arrau Méndez', 'Centro de Salud Familiar Arrau Méndez'),
        ('SAR', 'SAR'),
        ('Hospital San José', 'Hospital San José'),
        ('Centro Comunitario de Salud Familiar Buenos Aires', 'Centro Comunitario de Salud Familiar Buenos Aires'),
        ('Departamento de Salud Municipal Parral', 'Departamento de Salud Municipal Parral'),
    ]

    USER_TYPE_CHOICES = [
        ('usuario_normal', 'Usuario Normal'),
        ('admin', 'Administrador'),
        ('personal_administrativo', 'Personal Administrativo'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("Nombre completo", max_length=100)
    rut = models.CharField("RUT", max_length=12)
    position = models.CharField("Cargo", max_length=50, choices=CARGO_CHOICES, null=True, blank=True)
    establishment = models.CharField("Establecimiento", max_length=100, choices=DEPARTAMENTO_CHOICES, null=True, blank=True)
    user_type = models.CharField("Tipo de Usuario", max_length=50, choices=USER_TYPE_CHOICES, default='usuario_normal')
    permissions = models.CharField("Permisos", max_length=100, null=True, blank=True)
    firma = models.ImageField("Firma", upload_to='firmas/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"



class PermissionRequest(models.Model):
    # Opciones específicas para el estado y tipo de solicitud
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('autorizado', 'Autorizado'),
        ('no_autorizado', 'No Autorizado'),
        ('completado', 'Completado'),
    ]

    # Relaciones y datos básicos del usuario que realiza la solicitud
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="permission_requests")
    full_name = models.CharField("Nombre completo", max_length=100)
    rut = models.CharField("RUT", max_length=12)
    position = models.CharField("Cargo", max_length=50, choices=UserProfile.CARGO_CHOICES)
    establishment = models.CharField("Establecimiento", max_length=100, choices=UserProfile.DEPARTAMENTO_CHOICES)
    
    # Detalles específicos de la solicitud
    request_type = models.CharField("Tipo de Solicitud", max_length=20, choices=[
        ('FERIADO', 'Solicitud de Feriado Legal'),
        ('ADMINISTRATIVO', 'Permiso Administrativo'),
        ('COMPENSACION', 'Compensación de Tiempo'),
    ], default='FERIADO')
    number_of_days = models.PositiveIntegerField("Número de días", blank=True, null=True)
    date_from = models.DateField("Fecha desde")
    date_to = models.DateField("Fecha hasta")
    period = models.CharField("Periodo", max_length=50, blank=True, null=True)

    # Campos administrativos y de seguimiento
    autorizado = models.BooleanField("Autorizado", default=False)
    anticipado = models.BooleanField("Anticipado", default=False)
    postergado = models.BooleanField("Postergado", default=False)
    additional_date_from = models.DateField("Fecha adicional desde", null=True, blank=True)
    additional_date_to = models.DateField("Fecha adicional hasta", null=True, blank=True)
    firma_funcionario = models.FileField("Firma del funcionario", upload_to='firmas/', null=True, blank=True)
    estado = models.CharField("Estado", max_length=13, choices=ESTADO_CHOICES, default='pendiente')  # Incrementado a 13 caracteres

    # Campos adicionales
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    def save(self, *args, **kwargs):
        # Calcula automáticamente el número de días si las fechas están definidas
        if self.date_from and self.date_to:
            self.number_of_days = (self.date_to - self.date_from).days + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.request_type} - {self.number_of_days} días desde {self.date_from} - Estado: {self.estado}"


class PermissionRequestAdmin(models.Model):
    CARGO_CHOICES = UserProfile.CARGO_CHOICES
    DEPARTAMENTO_CHOICES = UserProfile.DEPARTAMENTO_CHOICES
    ESTADO_CHOICES = PermissionRequest.ESTADO_CHOICES
    JORNADA_CHOICES = [
        ("Completa", "Completa"),
        ("Mañana", "Mañana"),
        ("Tarde", "Tarde"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField("Nombre completo", max_length=100)
    rut = models.CharField("RUT", max_length=12)
    position = models.CharField("Cargo", max_length=50, choices=CARGO_CHOICES)
    establishment = models.CharField("Establecimiento", max_length=100, choices=DEPARTAMENTO_CHOICES)
    number_of_days = models.PositiveIntegerField("Número de días")
    date_from = models.DateField("Fecha desde")
    date_to = models.DateField("Fecha hasta")
    jornada = models.CharField("Jornada", max_length=50, choices=JORNADA_CHOICES, default="Completa")
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default="pendiente")
    firma_funcionario = models.ImageField("Firma del funcionario", upload_to="firmas/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.position}"



class CompensationRequest(models.Model):
    ESTADO_CHOICES = PermissionRequest.ESTADO_CHOICES

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField("Nombre completo", max_length=100)
    rut = models.CharField("RUT", max_length=12)
    position = models.CharField("Cargo", max_length=50, choices=UserProfile.CARGO_CHOICES)
    establishment = models.CharField("Establecimiento", max_length=100, choices=UserProfile.DEPARTAMENTO_CHOICES)
    number_of_hours = models.PositiveIntegerField("Número de horas")
    date_from = models.DateField("Fecha desde")
    date_to = models.DateField("Fecha hasta")
    time_from = models.TimeField("Horario desde")
    time_to = models.TimeField("Horario hasta")
    estado = models.CharField("Estado", max_length=13, choices=ESTADO_CHOICES, default='pendiente')  # Incrementado a 13 caracteres
    firma_funcionario = models.FileField("Firma del funcionario", upload_to='firmas/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.number_of_hours} horas desde {self.date_from}"



class Permission(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('feriado', 'Solicitud de Feriado Legal'),
        ('administrativo', 'Permiso Administrativo'),
        ('compensacion', 'Compensación de Tiempo'),
    ]

    full_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    date_from = models.DateField()
    date_to = models.DateField()
    estado = models.CharField(max_length=20, default='pendiente')
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES, default='FERIADO')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_request_type_display()}"