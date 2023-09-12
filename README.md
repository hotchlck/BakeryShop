# BakeryShop - Fresh Baked Goods Everyday!
[BakeryShop App](https://bakeryshop.adaptable.app/main/)

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
  - Template : Bertanggung jawab penuh terhadap User Interface. Mengelola komponen - 
               komponen statis dari halaman web, termasuk HTML yang dilihat oleh user.
- MVVM
  - Model : Komponen utama dari arsitektur yang mengelola data dan logika aplikasi.
  - View  : Menampilkan data dari model dan menyediakan berbagai representasi data pada 
            User Interface.
  - ViewModel : Perantara Model dan View yang mengimplementasikan & mengekspos properti   
                dan perintah publik yang digunakan oleh View melalui data binding.

Pada MVC, Model, View dan Controller merupakan tiga bagian yang terpisah. MVT mirip dengan MVC namun sering digunakan dalam framework web Django. Sementara itu, MVVM memisahkan logika domain dan tampilan aplikasi. 

