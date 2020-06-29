# Generated by Django 3.0 on 2020-06-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0083_auto_20200604_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daftar',
            name='basic_currency',
        ),
        migrations.RemoveField(
            model_name='daftar',
            name='premium_currency',
        ),
        migrations.RemoveField(
            model_name='daftar',
            name='standard_currency',
        ),
        migrations.RemoveField(
            model_name='minta',
            name='upah_currency',
        ),
        migrations.AlterField(
            model_name='daftar',
            name='basic',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='daftar',
            name='premium',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='daftar',
            name='standard',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='minta',
            name='upah',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]