# Generated by Django 3.0 on 2020-05-10 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0024_auto_20200511_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daftar',
            name='email',
        ),
        migrations.RemoveField(
            model_name='daftar',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='daftar',
            name='telepon',
        ),
    ]
