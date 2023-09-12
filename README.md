# BakeryShop - Fresh Baked Goods Everyday!
[BakeryShop App](https://bakeryshop.adaptable.app/main/)

## Pembuatan App BakeryShop
1. Membuat sebuah proyek Django baru
   - Membuat direktori dengan nama BakeryShop dan membuka command prompt di direktori 
     tersebut.
   - Membuat Virtual Environment baru dengan menjalankan command  
     ``` python -m venv env ``` . Lalu mengaktifkannya dengan command
     ```env\Scripts\activate.bat```.
   - Membuat file dengan nama requirements.txt di direktori yang sama dan menambahkan dependencies yang perlu di install di Visual Studio Code:
     ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
     ```
    Setelah itu Install dependencies dengan command ```pip install -r requirements.txt```. 

   - Membuat proyek Django baru dengan nama BakeryShop dengan command ```django-admin startproject BakeryShop .```.
   - Membuka file settings.py yang ada dalam direktori BakeryShop dan menambahkan tanda ```"*"``` pada ```ALOWED_HOST``` sehingga menjadi 
     ```ALLOWED_HOSTS = ["*"]```. Hal ini dilakukan untuk mengizinkan akses dari semua host sehingga aplikasi dapat diakses secara luas.
   - Menjalankan command ```python manage.py runserver``` untuk mengecek apakah proyek Django berjalan.
2. Membuat aplikasi dengan nama main pada proyek BakeryShop.
   - Membuka command prompt di direktori utama BakeryShop dan mengaktifkan virtual environment.
   - Menjalankan command  ```python manage.py startapp main``` untuk membuat aplikasi baru dengan nama main.
   - Mendaftarkan aplikasi main ke dalam proyek dengan menambahkan aplikasi main di daftar aplikasi yang ada di file settings.py
     ```
     INSTALLED_APPS = [
     ...,
     'main',
      ...
     ]
     ```
   - Membuat direktori dengan nama templates dan membuat file dengan nama main.html di dalam direktori tersebut. File main.html 
     berisi code html 
     yang akan menjadi tampilan utama halaman web aplikasi.
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
   - Membuka file urls.py dalam direktori main dan mengisinya dengan
     ```
     from django.urls import path
     from main.views import show_main

     app_name = 'main'

     urlpatterns = [
     path('', show_main, name='show_main'),
     ]
     ```
   - Membuka berkas urls.py dalam direktori proyek BakeryShop dan menambahkan import ```from django.urls import path, include```.
   - Menambahkan rute URL dalam variable urlpatterns untuk mengarahkan ke tampilan main. 
     ```
     urlpatterns = [
     ...
     path('main/', include('main.urls')),
     ...
     ]
     ```
4.  Membuat model Item pada aplikasi main.
    - Membuat class item yang berisi attribute :
      ```
      class item(models.Model):
      name = models.CharField(max_length=255)
      amount = models.IntegerField()
      description = models.TextField()
      price = models.IntegerField()
      type = models.CharField(max_length = 255)
      date_added =  models.DateField(auto_now_add=True, name="date_added")
      ```
    - Menjalankan command ```python manage.py makemigrations``` dan  ```ppython manage.py migrate``` untuk melakukan migrasi 
     agar perubahan model dapat dilacak Django.
5. Memodifikasi file views.py.
   - Menambahkan import ```from django.shortcuts import render```.
   - Membuat fungsi show-main yang berisi data yang akan ditampilkan di halaman web oleh html.
     ```
     def show_main(request):
        context = {
           'name': 'Salma Kurnia Dewi',
           'class': 'PBP B',
           'product' : 'BakeryShop'
       }

       return render(request, "main.html", context)
      ```
6. Melakukan deployment ke Adaptable
   - Menambahkan file .gitignore pada direktori utama BakeryShop yang berisi daftar file yang akan diabaikan saat melakukan pull, push, dan commit.
   - Melakukan add, commit, dan push untuk memperbarui repositori Github dengan perubahan yang dilakukan pada direktori lokal.
   - Melakukan deployment project melalui adaptable sesuai ketentuan tutorial.

## Request Client 
![baganClientRequest](https://github.com/hotchlck/BakeryShop/assets/126342746/c746edbf-7baa-4e7b-8b7f-8ceb6b1eeb5d)

## Virtual Environment
Virtual Environment merupakan tools untuk membuat lingkungan python virtual yang terisolasi. 
Virtual Environment membantu kita ketika membutuhkan dependencies yang berbeda - beda (contohnya python version) antara setiap proyek yang berjalan pada satu sistem operasi yang sama sehingga dapat mencegah konflik dan masalah yang disebabkan oleh perbedaan python version.
Aplikasi web berbasis Django tetap bisa dibuat tanpa Virtual Environment. 
Namun, terdapat risiko terjadinya konflik dependencies dengan proyek - proyek lain di sistem yang sama. 

## Mengenai MVC, MVT, dan MVVM
Ketiganya merupakan arsitektur yang digunakan untuk merancang dan mengembangkan aplikasi berbasis web. Arsitektur tersebut digunakan untuk memisahkan tanggung jawab antara visualisasi, pemrosesan, dan manajemen data untuk aplikasi User interface. 
- MVC
  - Model : Komponen utama dari arsitektur yang mengelola data dan logika aplikasi.
  - View  : Menampilkan data dari model dan menyediakan berbagai representasi data pada 
            User Interface.
  - Controller : Pengendali yang menghubungkan model dan view. 
- MVT
  - Model : Komponen utama dari arsitektur yang mengelola data dan logika aplikasi.
  - View  : Menampilkan data dari model dan menyediakan berbagai representasi data pada 
            User Interface.
  - Template : Bertanggung jawab penuh terhadap User Interface. Mengelola komponen - komponen statis dari halaman web,
               termasuk HTML yang dilihat oleh user.
- MVVM
  - Model : Komponen utama dari arsitektur yang mengelola data dan logika aplikasi.
  - View  : Menampilkan data dari model dan menyediakan berbagai representasi data pada 
            User Interface.
  - ViewModel : Perantara Model dan View yang mengimplementasikan & mengekspos properti   
                dan perintah publik yang digunakan oleh View melalui data binding.

Pada MVC, Model, View dan Controller merupakan tiga bagian yang terpisah. MVT mirip dengan MVC namun sering digunakan dalam framework web Django. Sementara itu, MVVM memisahkan logika domain dan tampilan aplikasi. 

