# Generated by Django 4.1.6 on 2023-03-05 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name']},
        ),
    ]