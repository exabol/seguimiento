# Generated by Django 3.2.8 on 2022-07-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0023_alter_actividades_fechainicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrodocumento', models.PositiveIntegerField(verbose_name='Nro de Documento')),
                ('extension', models.CharField(blank=True, max_length=2, verbose_name='Extensión')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('primerapellido', models.CharField(blank=True, max_length=40, verbose_name='Primer Apellido')),
                ('nomsegundoapellido', models.CharField(max_length=40, verbose_name='Segundo apellido')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('fechaCumpleanos', models.DateField(blank=True, null=True, verbose_name='Fecha Nacimiento')),
                ('fechaIngreso', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')),
                ('nroItem', models.PositiveIntegerField(verbose_name='Numero de ITEM')),
                ('codUnidEducativa', models.PositiveIntegerField(verbose_name='Código Unidad Educativa')),
                ('nroServicio', models.PositiveIntegerField(verbose_name='Número de Servicio')),
            ],
        ),
    ]
