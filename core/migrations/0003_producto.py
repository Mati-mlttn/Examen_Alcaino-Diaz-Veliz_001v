# Generated by Django 4.0.5 on 2022-07-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contacto111_dudas'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
    ]