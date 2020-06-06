# Generated by Django 3.0 on 2020-06-04 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tukangkuapp', '0092_auto_20200604_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdirectauthor',
            name='to_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
