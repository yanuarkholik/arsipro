# Generated by Django 2.2.10 on 2020-07-02 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0075_auto_20200702_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='user',
        ),
        migrations.RemoveField(
            model_name='requestdirectauthor',
            name='judul',
        ),
        migrations.RemoveField(
            model_name='requestdirectauthor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sellergigsimage',
            name='user',
        ),
        migrations.DeleteModel(
            name='Gigs',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='RequestDirectAuthor',
        ),
        migrations.DeleteModel(
            name='SellerGigsImage',
        ),
    ]
