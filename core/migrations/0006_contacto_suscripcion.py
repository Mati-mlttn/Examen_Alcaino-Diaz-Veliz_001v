# Generated by Django 4.0.5 on 2022-07-08 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_dudas_contacto_mensaje_contacto_tipo_consulta'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='suscripcion',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]