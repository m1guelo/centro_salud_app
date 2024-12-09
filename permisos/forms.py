from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PermissionRequest, PermissionRequestAdmin, CompensationRequest, UserProfile

# Formulario de Registro de Usuario (Crea User y UserProfile)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    full_name = forms.CharField(max_length=100, required=True, label="Nombre Completo")
    rut = forms.CharField(max_length=12, required=True, label="RUT")
    user_type = forms.ChoiceField(
        choices=UserProfile.USER_TYPE_CHOICES,
        label="Tipo de Usuario",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Crear o actualizar el perfil de usuario relacionado
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'full_name': self.cleaned_data['full_name'],
                    'rut': self.cleaned_data['rut'],
                    'user_type': self.cleaned_data['user_type'],
                },
            )
        return user

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email or "@" not in email:
            raise forms.ValidationError("Ingrese un correo electrónico válido.")
        return email

    def clean_rut(self):
        rut = self.cleaned_data.get("rut")
        # Eliminar puntos y guiones para validar numéricamente
        normalized_rut = rut.replace(".", "").replace("-", "")
        if not normalized_rut.isdigit() or len(normalized_rut) < 8:
            raise forms.ValidationError("El RUT debe ser numérico y tener al menos 8 dígitos.")
        return rut


# Formulario de Perfil de Usuario (Edición)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'rut', 'position', 'establishment', 'user_type', 'firma']
        labels = {
            'full_name': 'Nombre completo',
            'rut': 'RUT',
            'position': 'Cargo',
            'establishment': 'Establecimiento',
            'user_type': 'Tipo de Usuario',
            'firma': 'Firma',
        }

# Formulario de Solicitud de Permiso (Usuarios Normales)
class UserPermissionRequestForm(forms.ModelForm):
    class Meta:
        model = PermissionRequest
        fields = [
            'full_name', 'rut', 'position', 'establishment',
            'date_from', 'date_to', 'period', 'firma_funcionario',
        ]
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            profile = user.userprofile
            self.fields['full_name'].initial = profile.full_name
            self.fields['rut'].initial = profile.rut
            self.fields['position'].initial = profile.position
            self.fields['establishment'].initial = profile.establishment

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get("date_from")
        date_to = cleaned_data.get("date_to")

        if date_from and date_to and date_from > date_to:
            raise forms.ValidationError("La fecha de inicio no puede ser posterior a la fecha de término.")
        return cleaned_data

# Formulario de Gestión de Permisos (Administrativos)
class AdminPermissionForm(forms.ModelForm):
    class Meta:
        model = PermissionRequest
        fields = [
            'autorizado', 'anticipado', 'postergado', 
            'additional_date_from', 'additional_date_to', 
            'firma_funcionario'
        ]
        widgets = {
            'additional_date_from': forms.DateInput(attrs={'type': 'date'}),
            'additional_date_to': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulario para Permisos Administrativos
class AdminPermissionRequestForm(forms.ModelForm):
    class Meta:
        model = PermissionRequestAdmin
        fields = [
            "full_name", "rut", "position", "establishment",
            "number_of_days", "date_from", "date_to",
            "jornada", "firma_funcionario",
        ]
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

# Formulario de Solicitudes de Compensación
class CompensationRequestForm(forms.ModelForm):
    class Meta:
        model = CompensationRequest
        fields = [
            'full_name', 'rut', 'position', 'establishment',
            'number_of_hours', 'date_from', 'date_to',
            'time_from', 'time_to', 'firma_funcionario'
        ]
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
            'time_from': forms.TimeInput(attrs={'type': 'time'}),
            'time_to': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            profile = user.userprofile
            self.fields['full_name'].initial = profile.full_name
            self.fields['rut'].initial = profile.rut
            self.fields['position'].initial = profile.position
            self.fields['establishment'].initial = profile.establishment

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    full_name = forms.CharField(max_length=100, required=True, label="Nombre Completo")
    rut = forms.CharField(max_length=12, required=True, label="RUT")
    user_type = forms.ChoiceField(
        choices=UserProfile.USER_TYPE_CHOICES,
        label="Tipo de Usuario",
    )
    position = forms.ChoiceField(
        choices=UserProfile.CARGO_CHOICES,
        required=False,
        label="Cargo",
    )
    establishment = forms.ChoiceField(
        choices=UserProfile.DEPARTAMENTO_CHOICES,
        required=False,
        label="Establecimiento",
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop("profile", None)  # Se pasa el perfil explícitamente
        super().__init__(*args, **kwargs)
        if self.profile:
            self.fields["full_name"].initial = self.profile.full_name
            self.fields["rut"].initial = self.profile.rut
            self.fields["user_type"].initial = self.profile.user_type
            self.fields["position"].initial = self.profile.position
            self.fields["establishment"].initial = self.profile.establishment

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if self.profile:
                # Actualizamos los campos del perfil relacionado
                self.profile.full_name = self.cleaned_data["full_name"]
                self.profile.rut = self.cleaned_data["rut"]
                self.profile.user_type = self.cleaned_data["user_type"]
                self.profile.position = self.cleaned_data.get("position")
                self.profile.establishment = self.cleaned_data.get("establishment")
                self.profile.save()
        return user
