# Generated by Django 3.0 on 2020-06-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0096_auto_20200605_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='buat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
