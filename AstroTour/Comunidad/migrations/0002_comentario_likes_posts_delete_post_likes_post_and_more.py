# Generated by Django 4.0.3 on 2022-04-30 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
        ('Comunidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=140)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.astroturista')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_post', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('texto', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagen')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.astroturista')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='likes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Comunidad.posts'),
        ),
        migrations.AddField(
            model_name='likes',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.astroturista'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Comunidad.posts'),
        ),
    ]