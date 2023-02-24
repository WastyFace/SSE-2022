# Generated by Django 3.0.8 on 2023-02-23 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sse_app', '0010_auto_20211105_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')])),
                ('correo_uv', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')])),
            ],
        ),
    ]