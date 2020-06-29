# Generated by Django 3.0 on 2020-05-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0064_daftar_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='daftar',
            name='judul',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='daftar',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]