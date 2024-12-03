# Generated by Django 5.1.3 on 2024-11-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0004_remove_permissionrequestadmin_comp_date_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='con_goce_remuneracion',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='sin_goce_remuneracion',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='solicita_permiso_administrativo',
        ),
        migrations.RemoveField(
            model_name='permissionrequestadmin',
            name='user',
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='date_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='date_to',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='establishment',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='firma_funcionario',
            field=models.ImageField(blank=True, null=True, upload_to='firmas/'),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='jornada',
            field=models.CharField(choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde')], max_length=50),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='number_of_days',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='position',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='rut',
            field=models.CharField(max_length=12),
        ),
    ]
