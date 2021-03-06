# Generated by Django 3.0.7 on 2020-06-18 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Droga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('cantidad', models.IntegerField(unique=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='farmacia.Empresa')),
            ],
            options={
                'unique_together': {('nombre', 'cantidad')},
            },
        ),
    ]
