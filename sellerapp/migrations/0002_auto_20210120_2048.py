# Generated by Django 3.1.5 on 2021-01-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='request',
            name='kota',
        ),
        migrations.RemoveField(
            model_name='request',
            name='provinsi',
        ),
        migrations.AlterField(
            model_name='request',
            name='buat',
            field=models.DateField(auto_now_add=True),
        ),
    ]
