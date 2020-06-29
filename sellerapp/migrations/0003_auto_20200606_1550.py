# Generated by Django 3.0 on 2020-06-06 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0097_auto_20200605_1936'),
        ('sellerapp', '0002_auto_20200606_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellerProfile', to='tukangkuapp.Profile'),
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]