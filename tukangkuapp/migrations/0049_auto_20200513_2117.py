# Generated by Django 3.0 on 2020-05-13 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0048_auto_20200513_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daftar',
            old_name='user',
            new_name='author',
        ),
    ]