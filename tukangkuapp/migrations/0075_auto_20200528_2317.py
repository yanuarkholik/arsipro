# Generated by Django 3.0 on 2020-05-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0074_auto_20200528_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestdirectauthor',
            old_name='user',
            new_name='to_author',
        ),
    ]
