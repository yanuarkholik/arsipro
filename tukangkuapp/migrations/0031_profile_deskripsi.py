# Generated by Django 3.0 on 2020-05-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0030_remove_profile_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='deskripsi',
            field=models.TextField(blank=True, null=True),
        ),
    ]