# Generated by Django 3.0.7 on 2020-06-28 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sellerapp', '0055_auto_20200627_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=100)),
                ('nama_belakang', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('kontak', models.CharField(max_length=14)),
                ('deskripsi', models.TextField()),
                ('link', models.URLField()),
                ('jenis_ruangan', models.CharField(choices=[('Jenis Ruangan', 'Jenis Ruangan'), ('Kamar Tidur', 'Kamar Tidur'), ('Kamar Mandi', 'Kamar Mandi'), ('Dapur', 'Dapur'), ('Ruang Keluarga', 'Ruang Keluarga'), ('Taman', 'Taman'), ('Tangga', 'Tangga'), ('Ruang Makan', 'Ruang Makan'), ('Exterior', 'Exterior'), ('Ruang Belajar', 'Ruang Belajar'), ('Ruang Kerja', 'Ruang Kerja'), ('Perpustakaan', 'Perpustakaan')], default='Jenis Ruangan', max_length=50)),
                ('files', models.FileField(upload_to='upload/files/')),
                ('image', models.ImageField(upload_to='upload/display/')),
                ('services', models.CharField(choices=[('Kategori', 'Kategori'), ('Arsitek', 'Arsitek'), ('Design Interior', 'Design Interior'), ('Kontraktor', 'Kontraktor'), ('Design and Build', 'Design and Build')], default='Pilihan Service', max_length=50)),
                ('jumlah_budget', models.PositiveIntegerField(default=0)),
                ('alamat', models.CharField(max_length=500)),
                ('kota', models.CharField(max_length=50)),
                ('provinsi', models.CharField(choices=[('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh'), ('Aceh', 'Aceh')], default='Aceh', max_length=50)),
                ('status', models.CharField(choices=[('Dalam antrian', 'Dalam Antrian'), ('Dalam Pengerjaan', 'Dalam Pengerjaan'), ('Selesai', 'Selesai')], default='Dalam Antrian', max_length=30)),
                ('buat', models.DateField(auto_now=True)),
                ('tanggal_pengerjaan', models.DateField(auto_now_add=True)),
                ('tanggal_selesai', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('oleh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='karyawanUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data - Permintaan',
            },
        ),
    ]
