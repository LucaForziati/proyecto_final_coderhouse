# Generated by Django 4.0.3 on 2022-04-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viajes', '0004_destino_descripcion_vehiculo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
