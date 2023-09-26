# BakeryShop - Fresh Baked Goods Everyday!

# TUGAS 2
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

# TUGAS 3
## Implementasi Checklist
1. Mengatur routing dan membuat skeleton sebagai kerangka views
   - Mengubah berkas ```urls.py``` yang terletak pada subdirektori BakeryShop dan mengubah path pada url patterns dari 
     ```main/``` menjadi ''. 
     ```path('', include('main.urls')),```
   - Membuat folder ```templates``` pada direktori utama dan membuat berkas HTML dengan nama ```base.html``` dan mengisi berkas tersebut dengan kerangka umum untuk halaman web .
     ```
     {% load static %}
     <!DOCTYPE html>
     <html lang="en">
        <head>
           <meta charset="UTF-8" />
           <meta
             name="viewport"
             content="width=device-width, initial-scale=1.0"
            />
           {% block meta %}
           {% endblock meta %}
        </head>
        <body>
           {% block content %}
           {% endblock content %}
        </body>
     </html>
     ```
   - Membuka berkas ```settings.py``` yang terletak di subdirektori ```BakeryShop``` dan mengganti kode ```TEMPLATES``` agar 
     base.html terdeteksi sebagai template
     ```
       TEMPLATES = [
         {
             'BACKEND': 'django.template.backends.django.DjangoTemplates',
             'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
             'APP_DIRS': True,
             ...
       }
      ]
     ```
   - Mengubah kode berkas ```main.html``` yang terletak di subdirektori ```templates``` yang juga terletak dalam direktori 
     ```main```. 
     ```
      {% extends 'base.html' %}
       {% block content %}
          <h1>Shopping List Page</h1>
   
          <h5>Name:</h5>
          <p>{{name}}</p>
   
          <h5>Class:</h5>
          <p>{{class}}</p>
       {% endblock content %}
     ```
2. Membuat Form Input Data 
   - Membuat berkas baru dengan nama ```forms.py``` di dalam direktori ```main``` dan menambahkan beberapa kode berikut : 
     ```
      from django.forms import ModelForm
      from main.models import Product
      class ProductForm(ModelForm):
       class Meta:
       model = item
       fields = ["name","amount","description" "price", "type]
     ```
   Variable fields berisi objek model yang telah dibuat di berkas ```models.py``` .

3. Menampilkan data dalam bentuk HTML dan menambahkan fungsi ```views``` dalam format HTML, XML, JSON, XML by ID dan JSON by ID. 
   - Menambahkan import di berkas ```views.py``` di dalam direktori ```main```
     ```
     from django.http import HttpResponse
     from django.core import serializers
     from django.shortcuts import render
     from django.http import HttpResponseRedirect
     from main.forms import ProductForm
     from django.urls import reverse 
     from main.models import item
     ```
   - Menampilkan data dalam bentuk HTML. 
     - Membuat fungsi ```create_product``` dalam berkas ```views.py``` dengan parameter ```request``` yang berisi kumpulan kode 
       untuk membuat formulir yang dapat menyimpan data yang di-submit melalui form. 
       ```
       def create_product(request):
       form = ProductForm(request.POST or None)

       if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

       context = {'form': form}
       return render(request, "create_product.html", context)
       ```
     - Mengubah fungsi ```show_main``` dalam berkas ```views.py``` . Fungsi ini untuk menampilkan data dalam bentuk HTML.
       ```
       def show_main(request):
         items = item.objects.all()
         context = {
          'name': 'Salma Kurnia Dewi',
          'class': 'PBP B',
          'items' : items
         }
         return render(request, "main.html", context)
       ```
     - Menambahkan import pada berkas ```urls.py``` yang terdapat di direktori main.
       ```from main.views import show_main, create_product```
     - Menambahkan path url dalam ```urlpatterns``` di berkas yang sama. 
       ```path('create-product', create_product, name='create_product'),```
     - Membuat berkas berisi kode dengan nama ```create_product.html``` pada folder ```templates``` yang terletak di direktori 
       ```main``` . Isi berkas tersebut: 
       ```
        {% extends 'base.html' %} 
   
        {% block content %}
        <h1>Add New Item</h1>
   
        <form method="POST">
           {% csrf_token %}
           <table>
               {{ form.as_table }}
               <tr>
                   <td></td>
                   <td>
                       <input type="submit" value="Add Item"/>
                   </td>
               </tr>
           </table>
        </form>
   
        {% endblock %}
       ```
     - Menambahkan kode pada berkas ```main.html``` yang terletak di folder ```templates``` di direktori ```main```.
       ```
        <table>
           <tr>
             <th>Name</th>
             <th>Amount</th>
             <th>Description</th>
             <th>Price</th>
             <th>Type</th>
             <th>Date Added</th>
           </tr>
   
           {% for item in items %}
             <tr>
               <td>{{item.name}}</td>
               <td>{{item.amount}}</td>
               <td>{{item.description}}</td>
               <td>{{item.price}}</td>
               <td>{{item.type}}</td>
               <td>{{item.date_added}}</td>
             </tr>
           {% endfor %}
        </table>
   
        <br />
   
        <a href="{% url 'main:create_product' %}">
         <button>
           Add New Item
         </button>
        </a>
   
        {% endblock content %}
       ```

   - Membuat fungsi ```show_xml``` untuk menampilkan data dengan bentuk XML.
     ```
      def show_xml(request):
       data = item.objects.all()
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```
   - Membuat fungsi ```show_json``` untuk menampilkan data dengan bantuk JSON.
     ```
     def show_json(request):
       data = item.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```
   - Membuat fungsi ```show_xml_by_id``` untuk menampilkan data berdasarkan ID dalam bentuk XML.
     ```
     def show_xml_by_id(request, id):
       data = item.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```
   - Membuat fungsi ```show_json_by_id``` untuk menampilkan data berdasarkan ID dalam bentuk JSON.
     ```
     def show_json_by_id(request, id):
       data = item.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```
4. Membuat routing URL untuk masing - masing fungsi ```views```. 
   - Membuka berkas ```urls.py``` pada direktori ```main``` dan tambahkan import fungsi ```views```
     ```from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id ```
   - Menambahkan path url ke dalam ```urlpatterns``` untuk mengakses fungsi ```views``` yang sudah di-import.
     ```
     path('xml/', show_xml, name='show_xml'), 
     path('json/', show_json, name='show_json'), 
     path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
     path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
     ```
5. Mengecek data dengan mengakses fungsi ```views``` dengan URL menggunakan aplikasi Postman. 
   - Mengaktifkan env di dengan menjalankan perintah : 
     ```env\Scripts\activate.bat``` 
   - Menjalankan proyek Django dengan perintah :
     ```python manage.py runserver```
   - Membuka aplikasi postman dan membuat request baru dengan method ```GET``` dan memasukkan URL fungsi ```views```.
     - URL ```http://localhost:8000/```(HTML)
       ![Screenshot 2023-09-18 151003](https://github.com/hotchlck/BakeryShop/assets/126342746/3276793a-8eca-4d81-bf5f-772e81df6a09)
     - URL ```http://localhost:8000/xml``` dan ```http://localhost:8000/xml/1```
       ![Screenshot 2023-09-18 151039](https://github.com/hotchlck/BakeryShop/assets/126342746/f586821b-2c65-424f-9059-8b5db44bda31)
       ![Screenshot 2023-09-18 151137](https://github.com/hotchlck/BakeryShop/assets/126342746/f51da316-479d-4ef7-85b4-baed8d9a0a12)
     - URL ```http://localhost:8000/json``` dan ```http://localhost:8000/json/1```
       ![Screenshot 2023-09-18 151058](https://github.com/hotchlck/BakeryShop/assets/126342746/acbf04b9-8005-4fe5-ba40-4999947bb28e)
       ![Screenshot 2023-09-18 151120](https://github.com/hotchlck/BakeryShop/assets/126342746/b095f7b0-ebf4-406b-8ffb-1157b3d6552d)

## Perbedaan form POST dan form GET dalam Django
   - Metode ```POST``` digunakan untuk mengirim data ke server agar dapat membuat atau menulis ulang data. Data yang dikirimkan      ke server disimpan dalam ```HTTP```  request body sehingga data tidak ditampilkan di URL. Metode ini biasanya digunakan         untuk mengirimkan informasi yang sensitif. POST request tidak dapat di-cache dan tidak dapat di-bookmark. POST request          tidak membatasi panjang data sehingga cocok digunakan untuk data yang berukuran besar.
   - Metode ```GET``` digunakan untuk mengirim request pada server untuk mendapatkan data tertentu. Dengan menggunakan metode        ini, kita hanya bisa menerima data dari server dan tidak bisa mengubah-nya. Parameter request dari metode ```GET``` akan        ditampilkan di URL sehingga tidak dapat digunakan untuk mengolah data yang sensitif. ```GET``` request dapat di-cache dan       dapat di-bookmark. ```GET``` request memiliki batasan panjang data.

## Perbedaan XML, JSON, dan HTML dalam Pengiriman Data
   - XML 
     - Bahasa markup dan format berkas yang digunakan untuk menyimpan, mengirimkan, dan mengkonstruksi data, bukan untuk               menampilkan data. XML memiliki beberapa peraturan untuk mengkodekan dokumen dalam format yang dapat dibaca oleh mesin           dan manusia. Format XML lebih sulit dibaca jika dibandingkan dengan JSON. 
   - JSON
     - JSON memiliki format pertukaran data dengan teks yang mudah dibaca oleh manusia untuk menyimpan dan mengirimkan data            yang terdiri dari key-value pairs (dictionary) dan array. Jika dibandingkan dengan XML, format JSON yang berbasis pada          JavaSCript lebih mudah dibaca oleh komputer karena penulisannya yang lebih simpel. 
   - HTML
     - Bahasa markup yang digunakan untuk menyusun teks, gambar, dan materi lainnya yang akan ditampilkan oleh halaman web.

Perbedaan mendasar dari ketiganya adalah JSON dan XML merupakan metode alternatif untuk menyimpan dan mentransfer data,         sementara HTML digunakan untuk menyusun bagaimana data harus ditampilkan di perangkat pengguna.
     
## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   JSON sering digunakan dalam pertukaran data antar aplikasi karena mudah ditulis dan mudah dimengerti. JSON menggunakan          format dengan key-value pairs (dictionary) dan array. Tidak seperti XML, penulisan sintaks JSON lebih ringan dan tidak          membutuhkan tag khusus, atribut, atau skema tertentu sehingga mudah untuk diterjemahkan dan dibuat oleh komputer.

# TUGAS 3 
## Implementasi Checklist 
1. Fungsi registrasi, login, dan logout.
   - Mengaktifkan virtual environment
   - Fungsi register dan form register
     - Membuka berkas views.py pada direktori main dan menambahkan import
       ```
       from django.shortcuts import redirect
       from django.contrib.auth.forms import UserCreationForm
       from django.contrib import messages
       ```
     - Membuat fungsi register yang berisi kode untuk membuat formulir registrasi otomatis.
       ```
       def register(request):
          form = UserCreationForm()
      
          if request.method == "POST":
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
          context = {'form':form}
          return render(request, 'register.html', context)
       ```
     - Membuat berkas HTML yang bernama ```register.html``` pada folder ```main/templates``` yang bersisi kode berupa template untuk register account user.
       ```
         {% extends 'base.html' %}

         {% block meta %}
             <title>Register</title>
         {% endblock meta %}
         
         {% block content %}  
         
         <div class = "login">
             
             <h1>Register</h1>  
         
                 <form method="POST" >  
                     {% csrf_token %}  
                     <table>  
                         {{ form.as_table }}  
                         <tr>  
                             <td></td>
                             <td><input type="submit" name="submit" value="Daftar"/></td>  
                         </tr>  
                     </table>  
                 </form>
         
             {% if messages %}  
                 <ul>   
                     {% for message in messages %}  
                         <li>{{ message }}</li>  
                         {% endfor %}  
                 </ul>   
             {% endif %}
         
         </div>  
         
         {% endblock content %}
       ```
     - Import fungsi register dan menambahkan path url pada berkas ```urls.py``` yang terdapat di direktori ```main```
       ```from main.views import register```
       ```path('register/', register, name='register'), # ditambahkan pada urlpatterns ```
   - Fungsi login dan form login
     - Menambahkan import ```authenticate``` dan ```login``` serta membuat fungsi ```login_user``` berisi kode untuk mengautentikasikan input pengguna ketika
       ingin login.
       ```
       from django.contrib.auth import authenticate, login
       ...
       def login_user(request):
          if request.method == 'POST':
              username = request.POST.get('username')
              password = request.POST.get('password')
              user = authenticate(request, username=username, password=password)
              if user is not None:
                  login(request, user)
                  return redirect('main:show_main')
              else:
                  messages.info(request, 'Sorry, incorrect username or password. Please try again.')
          context = {}
          return render(request, 'login.html', context)
       ...
       ```
     - Membuat berkas dengan nama ```login.html``` pada folder ```main/templates``` yang berisi kode template.
       ```
         {% extends 'base.html' %}

         {% block meta %}
             <title>Login</title>
         {% endblock meta %}
         
         {% block content %}
         
         <div class = "login">
         
             <h1>Login</h1>
         
             <form method="POST" action="">
                 {% csrf_token %}
                 <table>
                     <tr>
                         <td>Username: </td>
                         <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                     </tr>
                             
                     <tr>
                         <td>Password: </td>
                         <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                     </tr>
         
                     <tr>
                         <td></td>
                         <td><input class="btn login_btn" type="submit" value="Login"></td>
                     </tr>
                 </table>
             </form>
         
             {% if messages %}
                 <ul>
                     {% for message in messages %}
                         <li>{{ message }}</li>
                     {% endfor %}
                 </ul>
             {% endif %}     
                 
             Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
         
         </div>
         
         {% endblock content %}
       ```
     - Import fungsi login dan menambahkan path url pada berkas ```urls.py``` yang terdapat di direktori ```main```
       ```from main.views import login_user```
       ```path('login/', login_user, name='login'), # ditambahkan pada urlpatterns ```
   - Fungsi logout
     - Menambahkan import ```logout``` dan membuat fungsi ```logout_user``` yang berisi
       ptotongan kode untuk implementasi fungsi logout.
       ```
       from django.contrib.auth import logout
       ...
       def logout_user(request):
       logout(request)
       return redirect('main:login')
       ...
       ```
     - Menambahkan kode button ```logout``` pada berkas ```main.html``` yang ada pafa folder ```main/templates```
       ```
       ...
       <a href="{% url 'main:logout' %}">
          <button>
              Logout
          </button>
       </a>
       ...
       ```
     - Import fungsi ```logout_user``` dan menambahkan path url pada berkas ```urls.py``` yang terdapat di direktori ```main```
       ```
       from main.views import logout_user
       ... 
       path('logout/', logout_user, name='logout'),
       ...
       ```
2. Membuat dua akun pengguna dengan tiga dummy data.
   ![Screenshot 2023-09-27 001800](https://github.com/hotchlck/BakeryShop/assets/126342746/0fdf1ba7-e2cf-42d5-8d4c-6beabd825fe2)
   ![Screenshot 2023-09-27 001952](https://github.com/hotchlck/BakeryShop/assets/126342746/936c0f11-3e16-4352-87f0-bce8cafbec3f)
3. Menampilkan detail informasi user yang sedang logged in berupa ```username``` dan menerapkan ```cookies``` yang berupa ```last login```
   - Menambahkan import ke dalam berkas ```views.py``` yang terdapat dalam direktori ```main```
     ```
     import datetime
     from django.http import HttpResponseRedirect
     from django.urls import reverse
     ```
   - Menambahkan cookie yang bernama ```last_login``` dalam fungsi ```login_user``` untuk menampilkan waktu terakhir user login.
     ```
     ...
      if user is not None:
          login(request, user)
          response = HttpResponseRedirect(reverse("main:show_main")) 
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response
     ...
     ```
     

          
   
## Pengertian Django ```UserCreationForm```
```UserCreationForm``` merupakan sistem autentikasi bawaan dari Django yang merupakan inheritance dari class ModelForm. Form ini digunakan untuk membuat form user baru. 
- Kelebihan :
  - Form merupakan template bawaan dari Django sehingga mudah digunakan.
  - ```UserCreationForm``` terintegrasi dengan database sehingga memudahkan penyimpanan data.
  - Form menyediakan validasi otomatis kepada input yang diberikan user saat membuat akun.
- Kekurangan
  - Kustomisasi sulit dilakukan dan membutuhkan penyesuaian yang lebih rumit.
  - Tampilan bawaan yang sederhana sehingga jika ingin merubah tampilan dapat menggunakan CSS dan HTML tambahan.
  - Fitur bawaan terbatas sehingga jika ingin menambah fitur autentikasi lainnya harus menambahkan secara manual.
    

   

