# Generated by Django 3.0 on 2020-06-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0078_auto_20200601_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdirectauthor',
            name='kirim_ke',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]