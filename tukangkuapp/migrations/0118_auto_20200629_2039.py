# Generated by Django 2.2.10 on 2020-06-29 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0117_auto_20200628_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gigs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profileGigs', to='sellerapp.Request'),
        ),
    ]