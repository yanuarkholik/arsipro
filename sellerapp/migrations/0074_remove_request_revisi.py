# Generated by Django 2.2.10 on 2020-07-02 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0073_auto_20200630_0133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='revisi',
        ),
    ]
