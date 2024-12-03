# Generated by Django 5.1.3 on 2024-11-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0011_userprofile_establishment_userprofile_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compensationrequest',
            name='position',
            field=models.CharField(choices=[('Dentista', 'Dentista'), ('Medico', 'Médico'), ('Quimico-Farmaceutico', 'Químico-Farmacéutico'), ('Asistente Social', 'Asistente Social'), ('Enfermera', 'Enfermera'), ('Kinesiologo', 'Kinesiólogo'), ('Matrona', 'Matrona'), ('Nutricionista', 'Nutricionista'), ('Psicologo', 'Psicólogo'), ('Tecnologo Medico', 'Tecnólogo Médico'), ('Fonoaudiologo', 'Fonoaudiólogo'), ('Terapeuta Ocupacional', 'Terapeuta Ocupacional'), ('Educadora de Parvulos', 'Educadora de Párvulos'), ('Profesor de Educacion Fisica', 'Profesor de Educación Física'), ('Abogado', 'Abogado'), ('Ingeniero en Informatica', 'Ingeniero en Informática'), ('Ingeniero en Prevencion de Riesgos', 'Ingeniero en Prevención de Riesgos'), ('Ingeniero en Administracion de Empresas', 'Ingeniero en Administración de Empresas'), ('Ingeniero Comercial', 'Ingeniero Comercial'), ('Contador Auditor', 'Contador Auditor'), ('TENS Enfermeria', 'TENS (Enfermería)'), ('TANS Administracion', 'TANS (Administración)'), ('Podologo', 'Podólogo'), ('Estadistico', 'Estadístico'), ('Programador', 'Programador/ Técnico en Computación'), ('Paramedico', 'Paramédico'), ('Secretaria', 'Secretaria'), ('Administrativos de Salud', 'Administrativos de Salud'), ('Auxiliar de Servicio', 'Auxiliar de Servicio'), ('Conductor', 'Conductor'), ('Estafeta', 'Estafeta'), ('Director de Consultorio', 'Director de Consultorio (CESFAM Arrau Méndez)'), ('Director de Departamento de Salud Municipal', 'Director de Departamento de Salud Municipal')], max_length=50, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='permissionrequest',
            name='position',
            field=models.CharField(choices=[('Dentista', 'Dentista'), ('Medico', 'Médico'), ('Quimico-Farmaceutico', 'Químico-Farmacéutico'), ('Asistente Social', 'Asistente Social'), ('Enfermera', 'Enfermera'), ('Kinesiologo', 'Kinesiólogo'), ('Matrona', 'Matrona'), ('Nutricionista', 'Nutricionista'), ('Psicologo', 'Psicólogo'), ('Tecnologo Medico', 'Tecnólogo Médico'), ('Fonoaudiologo', 'Fonoaudiólogo'), ('Terapeuta Ocupacional', 'Terapeuta Ocupacional'), ('Educadora de Parvulos', 'Educadora de Párvulos'), ('Profesor de Educacion Fisica', 'Profesor de Educación Física'), ('Abogado', 'Abogado'), ('Ingeniero en Informatica', 'Ingeniero en Informática'), ('Ingeniero en Prevencion de Riesgos', 'Ingeniero en Prevención de Riesgos'), ('Ingeniero en Administracion de Empresas', 'Ingeniero en Administración de Empresas'), ('Ingeniero Comercial', 'Ingeniero Comercial'), ('Contador Auditor', 'Contador Auditor'), ('TENS Enfermeria', 'TENS (Enfermería)'), ('TANS Administracion', 'TANS (Administración)'), ('Podologo', 'Podólogo'), ('Estadistico', 'Estadístico'), ('Programador', 'Programador/ Técnico en Computación'), ('Paramedico', 'Paramédico'), ('Secretaria', 'Secretaria'), ('Administrativos de Salud', 'Administrativos de Salud'), ('Auxiliar de Servicio', 'Auxiliar de Servicio'), ('Conductor', 'Conductor'), ('Estafeta', 'Estafeta'), ('Director de Consultorio', 'Director de Consultorio (CESFAM Arrau Méndez)'), ('Director de Departamento de Salud Municipal', 'Director de Departamento de Salud Municipal')], max_length=50, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='permissionrequestadmin',
            name='position',
            field=models.CharField(choices=[('Dentista', 'Dentista'), ('Medico', 'Médico'), ('Quimico-Farmaceutico', 'Químico-Farmacéutico'), ('Asistente Social', 'Asistente Social'), ('Enfermera', 'Enfermera'), ('Kinesiologo', 'Kinesiólogo'), ('Matrona', 'Matrona'), ('Nutricionista', 'Nutricionista'), ('Psicologo', 'Psicólogo'), ('Tecnologo Medico', 'Tecnólogo Médico'), ('Fonoaudiologo', 'Fonoaudiólogo'), ('Terapeuta Ocupacional', 'Terapeuta Ocupacional'), ('Educadora de Parvulos', 'Educadora de Párvulos'), ('Profesor de Educacion Fisica', 'Profesor de Educación Física'), ('Abogado', 'Abogado'), ('Ingeniero en Informatica', 'Ingeniero en Informática'), ('Ingeniero en Prevencion de Riesgos', 'Ingeniero en Prevención de Riesgos'), ('Ingeniero en Administracion de Empresas', 'Ingeniero en Administración de Empresas'), ('Ingeniero Comercial', 'Ingeniero Comercial'), ('Contador Auditor', 'Contador Auditor'), ('TENS Enfermeria', 'TENS (Enfermería)'), ('TANS Administracion', 'TANS (Administración)'), ('Podologo', 'Podólogo'), ('Estadistico', 'Estadístico'), ('Programador', 'Programador/ Técnico en Computación'), ('Paramedico', 'Paramédico'), ('Secretaria', 'Secretaria'), ('Administrativos de Salud', 'Administrativos de Salud'), ('Auxiliar de Servicio', 'Auxiliar de Servicio'), ('Conductor', 'Conductor'), ('Estafeta', 'Estafeta'), ('Director de Consultorio', 'Director de Consultorio (CESFAM Arrau Méndez)'), ('Director de Departamento de Salud Municipal', 'Director de Departamento de Salud Municipal')], max_length=50, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(blank=True, choices=[('Dentista', 'Dentista'), ('Medico', 'Médico'), ('Quimico-Farmaceutico', 'Químico-Farmacéutico'), ('Asistente Social', 'Asistente Social'), ('Enfermera', 'Enfermera'), ('Kinesiologo', 'Kinesiólogo'), ('Matrona', 'Matrona'), ('Nutricionista', 'Nutricionista'), ('Psicologo', 'Psicólogo'), ('Tecnologo Medico', 'Tecnólogo Médico'), ('Fonoaudiologo', 'Fonoaudiólogo'), ('Terapeuta Ocupacional', 'Terapeuta Ocupacional'), ('Educadora de Parvulos', 'Educadora de Párvulos'), ('Profesor de Educacion Fisica', 'Profesor de Educación Física'), ('Abogado', 'Abogado'), ('Ingeniero en Informatica', 'Ingeniero en Informática'), ('Ingeniero en Prevencion de Riesgos', 'Ingeniero en Prevención de Riesgos'), ('Ingeniero en Administracion de Empresas', 'Ingeniero en Administración de Empresas'), ('Ingeniero Comercial', 'Ingeniero Comercial'), ('Contador Auditor', 'Contador Auditor'), ('TENS Enfermeria', 'TENS (Enfermería)'), ('TANS Administracion', 'TANS (Administración)'), ('Podologo', 'Podólogo'), ('Estadistico', 'Estadístico'), ('Programador', 'Programador/ Técnico en Computación'), ('Paramedico', 'Paramédico'), ('Secretaria', 'Secretaria'), ('Administrativos de Salud', 'Administrativos de Salud'), ('Auxiliar de Servicio', 'Auxiliar de Servicio'), ('Conductor', 'Conductor'), ('Estafeta', 'Estafeta'), ('Director de Consultorio', 'Director de Consultorio (CESFAM Arrau Méndez)'), ('Director de Departamento de Salud Municipal', 'Director de Departamento de Salud Municipal')], max_length=50, null=True, verbose_name='Cargo'),
        ),
    ]
