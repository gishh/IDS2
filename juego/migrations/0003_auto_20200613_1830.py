# Generated by Django 3.0.7 on 2020-06-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0002_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
