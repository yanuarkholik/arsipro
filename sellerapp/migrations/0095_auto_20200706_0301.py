# Generated by Django 2.2.10 on 2020-07-05 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0094_auto_20200706_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='oleh',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='sellerapp.Request'),
        ),
    ]