# Generated by Django 3.2.9 on 2022-03-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmovies', '0003_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Sugerencia'], [3, 'Felicitaciones']]),
        ),
    ]
