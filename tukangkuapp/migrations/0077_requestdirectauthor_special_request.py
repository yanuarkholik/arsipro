# Generated by Django 3.0 on 2020-06-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0076_auto_20200601_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdirectauthor',
            name='special_Request',
            field=models.TextField(blank=True, null=True),
        ),
    ]
