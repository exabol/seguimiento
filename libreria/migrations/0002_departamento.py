# Generated by Django 3.2.8 on 2022-06-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=100, null=True, verbose_name='Departamento')),
            ],
        ),
    ]
