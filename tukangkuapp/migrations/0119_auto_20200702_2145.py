# Generated by Django 2.2.10 on 2020-07-02 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tukangkuapp', '0118_auto_20200629_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='deskripsi_singkat',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gigs',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nama_belakang',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nama_depan',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pendidikan',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pengalaman',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profesi',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sertifikasi',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='web',
        ),
    ]
