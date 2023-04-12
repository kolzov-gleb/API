# Generated by Django 4.1.6 on 2023-03-05 06:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('year_of_birth', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(17)])),
                ('year_of_manufacture', models.DecimalField(decimal_places=0, max_digits=4)),
                ('number_of_pages', models.DecimalField(decimal_places=0, max_digits=8)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
    ]