# Generated by Django 3.0 on 2020-05-11 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0034_minta_daftar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minta',
            name='daftar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tukangkuapp.Daftar'),
        ),
    ]