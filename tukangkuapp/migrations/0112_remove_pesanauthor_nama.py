
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0111_auto_20200622_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesanauthor',
            name='nama',
        ),
    ]
