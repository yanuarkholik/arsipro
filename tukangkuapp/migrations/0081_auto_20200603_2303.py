# Generated by Django 3.0 on 2020-06-03 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0080_auto_20200601_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postdaftarimage',
            old_name='file',
            new_name='user',
        ),
    ]
