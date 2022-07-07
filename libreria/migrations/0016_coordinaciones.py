# Generated by Django 3.2.8 on 2022-07-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0015_ilcs_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_coordinacion', models.CharField(max_length=30, null=True, verbose_name='Nombre Coordinación')),
                ('estado_coordinacion', models.BooleanField(default='1')),
            ],
            options={
                'verbose_name': 'Coordinacion',
                'verbose_name_plural': 'Coordinaciones',
                'db_table': 'coordinaciones',
                'ordering': ['nombre_coordinacion'],
            },
        ),
    ]