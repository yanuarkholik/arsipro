# Generated by Django 3.0 on 2020-05-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0063_remove_daftar_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='daftar',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
    ]