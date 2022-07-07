# Generated by Django 3.2.8 on 2022-06-29 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_departamentos_ilcs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamentos',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='ilcs',
            name='estado',
        ),
        migrations.AddField(
            model_name='departamentos',
            name='estado_dep',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ilcs',
            name='estado_ilc',
            field=models.BooleanField(default=True),
        ),
    ]
