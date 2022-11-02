# Generated by Django 3.0.8 on 2021-11-04 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sse_app', '0004_auto_20211104_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='celular',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Sólo se permiten números de teléfono de 10 dígitos.')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='correo',
            field=models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='correo_uv',
            field=models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')]),
        ),
    ]
