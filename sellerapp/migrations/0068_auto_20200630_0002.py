# Generated by Django 2.2.10 on 2020-06-29 17:02

from django.db import migrations, models
import sellerapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0067_request_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='emp_id',
            field=models.IntegerField(default=sellerapp.models.Request.ids, editable=False, unique=True, verbose_name='Code'),
        ),
    ]
