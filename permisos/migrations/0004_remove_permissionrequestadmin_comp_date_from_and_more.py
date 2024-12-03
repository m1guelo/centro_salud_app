# Generated by Django 5.1.3 on 2024-11-07 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0003_permissionrequestadmin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='comp_date_from',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='comp_date_to',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='comp_time_from',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='comp_time_to',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='number_of_hours',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='solicita_compensacion',
        ),
        migrations.CreateModel(
            name='CompensationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('rut', models.CharField(max_length=12, verbose_name='RUT')),
                ('position', models.CharField(max_length=50, verbose_name='Cargo')),
                ('establishment', models.CharField(max_length=100, verbose_name='Establecimiento')),
                ('number_of_hours', models.PositiveIntegerField(verbose_name='Número de horas')),
                ('date_from', models.DateField(verbose_name='Fecha desde')),
                ('date_to', models.DateField(verbose_name='Fecha hasta')),
                ('time_from', models.TimeField(verbose_name='Horario desde')),
                ('time_to', models.TimeField(verbose_name='Horario hasta')),
                ('firma_funcionario', models.FileField(blank=True, null=True, upload_to='firmas/', verbose_name='Firma del funcionario')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]