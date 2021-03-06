# Generated by Django 3.2.8 on 2022-06-30 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0010_auto_20220629_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamentos',
            options={'ordering': ['nombre_departamento'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.RenameField(
            model_name='ilcs',
            old_name='id',
            new_name='id_ilc',
        ),
        migrations.RemoveField(
            model_name='departamentos',
            name='estado_depa',
        ),
        migrations.RemoveField(
            model_name='departamentos',
            name='nombre_depa',
        ),
        migrations.AddField(
            model_name='departamentos',
            name='estado_departamento',
            field=models.BooleanField(default='1'),
        ),
        migrations.AddField(
            model_name='departamentos',
            name='nombre_departamento',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre Departamento'),
        ),
        migrations.AddField(
            model_name='ilcs',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libreria.departamentos'),
        ),
        migrations.AlterModelTable(
            name='departamentos',
            table='departamento',
        ),
    ]
