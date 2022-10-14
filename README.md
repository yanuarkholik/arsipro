# ArsiJob
Yanuar Nur Kholik 18.12.0974

Baca Big Note dibawah 

# Installation
Menggunakan [Python](https://www.python.org/downloads/)==3.9.1
Menggunakan Framwork Python [Django](https://docs.djangoproject.com/en/3.1/topics/install/)==3.1.5 atau bisa 
```python
pip install django==3.1.5
```

#### 1. Download [virtualenv](https://pypi.org/project/virtualenv/) untuk membuat Virtual Environment Django dengan command dibawah
```python
pip install virtualenv
```
*Note : aplikasi bisa berjalan tanpa virtualenv, virtualenv digunakan untuk mengoptimalkan development Python*
#### 2. Membuat virtualenv
```python
python venv nama_virtualenv
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
python manage.py makemigrations
python manage.py migrate # Akan memunculkan banyak "OK", berarti program tidak ada masalah
python manage.py runserver
```
Web aplikasi dapat di buka pada browser apa saja di  
```python 
# user page
127.0.0.1:8000
```

#### 6. Super admin page
```python 
puthon manage.py runserver

# ketikkan pada browser
127.0.0.1:8000/admin/
```
Username / pass
1. admin / 123
2. terminal >> python manage.py createsuperuser 
3. Sign Up

# Note
1. Super admin bisa mengganti permission
2. Main navigator ada di ```127.0.0.1:8000/admin/```
3. Seharusnya program bisa jalan karena sudah di reinstall beberapa kali pada direktori dan device berbeda
