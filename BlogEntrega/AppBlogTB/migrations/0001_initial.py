# Generated by Django 4.2.5 on 2023-09-29 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Escritor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('documento', models.IntegerField()),
                ('profesion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('documento', models.IntegerField()),
                ('profesion', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('cuerpo', models.CharField(max_length=30000)),
                ('anio_publicacion', models.IntegerField()),
                ('palabras_claves', models.CharField(max_length=20)),
                ('documento_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlogTB.escritor')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_comentario', models.CharField(max_length=40)),
                ('cuerpo', models.CharField(max_length=1200)),
                ('anio_publicacion', models.IntegerField()),
                ('documento_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlogTB.lector')),
                ('titulo_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBlogTB.paper')),
            ],
        ),
    ]