# Generated by Django 5.1.3 on 2024-11-27 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0022_compensationrequest_estado_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='permissionrequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Última actualización'),
        ),
        migrations.AlterField(
            model_name='compensationrequest',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('autorizado', 'Autorizado'), ('no_autorizado', 'No Autorizado'), ('completado', 'Completado')], default='pendiente', max_length=15),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='additional_date_from',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha adicional desde'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='additional_date_to',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha adicional hasta'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='establishment',
            field=models.CharField(choices=[('Posta de Salud Rural Villa Baviera', 'Posta de Salud Rural Villa Baviera'), ('Posta de Salud Rural Los Canelos', 'Posta de Salud Rural Los Canelos'), ('Posta de Salud Rural Bullileo', 'Posta de Salud Rural Bullileo'), ('Posta de Salud Rural Bajos de Huenutil', 'Posta de Salud Rural Bajos de Huenutil'), ('Posta de Salud Rural Catillo', 'Posta de Salud Rural Catillo'), ('Posta de Salud Rural Digua', 'Posta de Salud Rural Digua'), ('Posta de Salud Rural Monte Flor', 'Posta de Salud Rural Monte Flor'), ('Posta de Salud Rural San Alejo', 'Posta de Salud Rural San Alejo'), ('Posta de Salud Rural Talquita', 'Posta de Salud Rural Talquita'), ('Posta de Salud Rural Los Carros', 'Posta de Salud Rural Los Carros'), ('Posta de Salud Rural Perquilauquén', 'Posta de Salud Rural Perquilauquén'), ('Posta de Salud Rural La Orilla', 'Posta de Salud Rural La Orilla'), ('Posta de Salud Rural Fuerte Viejo', 'Posta de Salud Rural Fuerte Viejo'), ('Centro Comunitario de Salud Familiar Los Olivos', 'Centro Comunitario de Salud Familiar Los Olivos'), ('Centro de Salud Familiar Arrau Méndez', 'Centro de Salud Familiar Arrau Méndez'), ('SAR', 'SAR'), ('Hospital San José', 'Hospital San José'), ('Centro Comunitario de Salud Familiar Buenos Aires', 'Centro Comunitario de Salud Familiar Buenos Aires'), ('Departamento de Salud Municipal Parral', 'Departamento de Salud Municipal Parral')], max_length=100, verbose_name='Establecimiento'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('autorizado', 'Autorizado'), ('no_autorizado', 'No Autorizado'), ('completado', 'Completado')], default='pendiente', max_length=20, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='number_of_days',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de días'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='period',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permission_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('autorizado', 'Autorizado'), ('no_autorizado', 'No Autorizado'), ('completado', 'Completado')], default='pendiente', max_length=15),
        ),
    ]
