# Generated by Django 4.0.3 on 2022-04-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='gravedad',
            field=models.FloatField(),
        ),
    ]
