# arsipro
Yanuar Nur Kholik 18.12.0974

# Tugas
#### 1. Tugas membuat [rancangan db](https://github.com/yanuarkholik/arsipro/tree/main/screen_capture/db) dan [screen capture table](https://github.com/yanuarkholik/arsipro/tree/main/screen_capture/rancangan%20db)
Berisi screen capture table db dan rancangan db
#### 2. Tugas membuat halaman [login](https://github.com/yanuarkholik/arsipro/blob/main/templates/login/login.html) dan [screen capture halaman login](https://github.com/yanuarkholik/arsipro/blob/main/screen_capture/Login/Login.png)
Berisi screen capture halaman login dan source code halaman login
#### 3. Tugas membuat halaman [admin](https://github.com/yanuarkholik/arsipro/tree/main/templates/admin) dan [screen capture halaman admin](https://github.com/yanuarkholik/arsipro/tree/main/screen_capture/interface)
Berisi source code halaman admin dkk.
#### 4. Tugas membuat halaman [user](https://github.com/yanuarkholik/arsipro/blob/main/templates/base.html) dan screen [capture halaman user](https://github.com/yanuarkholik/arsipro/tree/main/screen_capture/interface)
Berisi source code halaman user dan screen capture halaman user dan admin.

# Installation
Menggunakan Framwork Python [Django](https://docs.djangoproject.com/en/3.1/topics/install/)

#### 1. Download [virtualenv](https://yasoob.me/2013/07/30/what-is-virtualenv/) untuk membuat Virtual Environment Django dengan command dibawah
```python
pip install virtualenv
```
*Note : aplikasi bisa berjalan tanpa virtualenv, virtualenv digunakan untuk mengoptimalkan development Python*
#### 2. Membuat virtualenv
```python
virtualenv nama_virtualenv
```
#### 3. Aktivasi virtualenv
```python
nama_virtualenv/Scripts/activate
```
#### 4. Install requirements.txt dengan command dibawah
```python 
pip install -r requirements.txt
```
Jika terjadi error atau ```requirements.txt``` tidak mau terinstall maka buka file ```requirements.txt``` install package/plugin satu-persatu dengan cara meng-copas nama dan versi package yang tertera. Contoh :
```python
pip install (nama_package==versi_package)
```
Kemudian hapus paket yang error tersebut pada ```requirements.txt``` untuk meninstall via requirements, jika ingin menginstall satu-persatu bisa pakai perintah diatas

#### 5. Menjalankan program
```python
python manage.py make migrations
python manage.py migrate # Akan memunculkan banyak "OK", berarti program tidak ada masalah
python manage.py runserver
```
Web aplikasi dapat di buka pada browser apa saja di  
```python 
# user page
127.0.0.1:8000

# admin page
127.0.0.1:8000/admin/
```

#### 6. Super admin page
```python 
puthon manage.py runserver

# ketikkan pada browser
127.0.0.1:8000/super-admin/
```
Username / pass
1. yanuar / 12345
2. yayan / 123


