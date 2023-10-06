# Generated by Django 4.2.5 on 2023-10-02 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogTB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='documento_autor',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='documento_comentarista',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='AppBlogTB.lector', to_field='documento'),
        ),
        migrations.AlterField(
            model_name='escritor',
            name='documento',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='lector',
            name='documento',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='documento_autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='AppBlogTB.escritor', to_field='documento'),
        ),
    ]
