# Generated by Django 4.1 on 2022-08-17 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_autor_post_categorias"),
    ]

    operations = [
        migrations.RenameModel(old_name="categorias", new_name="categoria",),
    ]