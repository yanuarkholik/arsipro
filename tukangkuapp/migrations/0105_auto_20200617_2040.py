# Generated by Django 2.2.10 on 2020-06-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0104_auto_20200617_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='deskripsi',
            field=models.TextField(blank=True, help_text='Deskripsi singkat Profile anda**', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='deskripsi_singkat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]