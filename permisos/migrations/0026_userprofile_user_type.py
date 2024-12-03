# Generated by Django 5.1.3 on 2024-12-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0025_alter_permissionrequestadmin_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('usuario_normal', 'Usuario Normal'), ('admin', 'Administrador'), ('personal_administrativo', 'Personal Administrativo')], default='usuario_normal', max_length=50, verbose_name='Tipo de Usuario'),
        ),
    ]