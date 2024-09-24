Nama : Nabilah Devina Mumin

NPM : 2306245876

Kelas : PBP B 

1.⁠ ⁠Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
-  ⁠Pertama-tama, kita buat proyek Django baru dengan nama "cutieshop". Proyek ini adalah kerangka kerja utama yang akan mengatur aplikasi dan pengaturannya. Pastikan proyek ini berada dalam direktori utama bernama "cutieshop" dan terhubung dengan repositori GitHub. Ini berfungsi untuk menyimpan kode di GitHub dan memantau perubahan yang dibuat.
-⁠  ⁠Selanjutnya, kita buat aplikasi baru di dalam proyek Django ini. Kita beri nama aplikasi ini "main".
-⁠  ⁠Agar aplikasi "main" dikenali oleh proyek "cutieshop", kita perlu mendaftarkannya. Buka file settings.py di proyek dan tambahkan nama "main" ke dalam daftar INSTALLED_APPS.
-⁠  ⁠Sekarang kita perlu mendefinisikan struktur data yang akan digunakan aplikasi. Buka file models.py di aplikasi "main" dan buat class bernama Product. Fungsi models.py adalah untuk menyimpan script database.
-  ⁠Buat folder baru dengan nama "templates" di dalam direktori aplikasi "main". Di dalam folder ini, buat file HTML bernama "main.html". File ini akan digunakan untuk mendefinisikan bagaimana data dari aplikasi ditampilkan kepada pengguna di halaman web.
- ⁠Buka file views.py dan tambahkan fungsi yang akan menghubungkan data dari model dengan template HTML yang kita buat. Fungsi ini akan mengambil data produk dan mengirimkannya ke template "main.html" untuk ditampilkan. Ini adalah cara aplikasi menunjukkan informasi kepada pengguna.
-  Di dalam aplikasi "main", buat file urls.py untuk mengatur URL yang akan mengarahkan pengguna ke tampilan yang tepat. 
-  ⁠Buka file urls.py di proyek "cutieshop" dan tambahkan rute yang mengarah ke file urls.py di aplikasi "main".
-⁠  ⁠Setelah semuanya siap, saatnya untuk Deployment ke PWS.

2. ![image](https://github.com/user-attachments/assets/e4c0e411-947a-4071-a468-9edcf59722e1)


3.⁠ ⁠Jelaskan fungsi git dalam pengembangan perangkat lunak!
•⁠  ⁠Mengelola Versi Kode: 
Git memudahkan pengembang melacak perubahan pada kode dengan menyimpannya sebagai "commit" setiap kali ada perubahan. Setiap commit dilengkapi pesan penjelas, sehingga pengembang bisa melihat perubahan yang telah dilakukan dan kembali ke versi sebelumnya jika diperlukan.
•⁠  ⁠Pengelolaan Repositori: 
Git digunakan untuk penyimpanan dan pengelolaan repositori baik di lokal komputer maupun server seperti github.
•⁠  ⁠Memudahkan kolaborasi Tim: 
Git memungkinkan banyak pengembang bekerja pada proyek yang sama tanpa saling mengganggu. Setiap orang bisa mengerjakan bagian berbeda secara bersamaan, dan Git akan menggabungkan perubahan dari berbagai cabang serta membantu menyelesaikan konflik jika ada.

4.⁠ ⁠Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
•⁠  ⁠Struktur dan sintaksnya sederhana sehingga memudahkan pembelajaran.
•⁠  ⁠Menggunakan pendekatan berbasis MVT sehingga membantu pemula mengerti konsep dasar pemisahan tanggung jawab dalam aplikasi. Hal ini sangat penting dalam pengembangan perangkat lunak skala besar.
•⁠  ⁠Integrasi Mudah sehingga dapat dengan mudah dihubungkan dengan berbagai teknologi lain.

5.⁠ ⁠Mengapa model pada Django disebut sebagai ORM?
Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai lapisan yang menghubungkan antara objek dalam kode Python dengan tabel dalam basis data relasional. ORM memungkinkan pengembang untuk bekerja dengan data menggunakan konsep objek dalam bahasa pemrograman, tanpa harus menulis SQL secara langsung untuk berinteraksi dengan basis data.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
TUGAS 3

1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery memungkinkan akses data yang tersimpan di server atau database pusat oleh pengguna di berbagai lokasi. Platform perlu terhubung dengan layanan eksternal seperti API untuk memastikan bahwa data yang dibutuhkan dapat dikirim dan diterima dalam format yang sesuai, sehingga mendukung interaksi dan kolaborasi yang mulus antara berbagai sistem. Hal ini juga memastikan bahwa proses pengiriman data berjalan dengan efisien, tepat waktu, dan konsisten untuk menjaga kelancaran operasional platform secara keseluruhan.

2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? 
Berikut perbedaan anatara XML dan JSON :
- Dalam hal integrasi dengan bahasa pemograman, JSON lebih mudah diintegrasikan dengan bahasa pemrograman seperti JavaScript, Python, dan Java. Sedangkan, XML membutuhkan parsing lebih rumit.
- Dalam hal kemudahan penggunaan, JSON mudah dibaca dan ditulis (mirip dengan struktur objek di banyak bahasa pemrograman). Sedangkan, XML lebih kompleks dan sulit dikelola.
- Dalam hal keringkasan, JSON lebih ringkas dan efisien dalam penggunaan bandwidth dan penyimpanan. Sedangkan, XML lebih panjang karena menggunakan banyak tag, seperti <element></element>.
Dari beberapa perbedaan diatas, dapat disimpulkan JSON lebih populer karena ringan, cepat, dan mudah digunakan. XML masih digunakan di beberapa kasus khusus, seperti standar industri dan dokumen kompleks.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memeriksa keabsahan data yang dikirimkan, memastikan bahwa input memenuhi aturan yang ditetapkan, seperti format email atau jenis data yang tepat. Jika ditemukan kesalahan, method ini akan menandai form sebagai tidak valid dan menyimpan pesan kesalahan untuk setiap field yang bermasalah, sehingga bisa ditampilkan kepada pengguna. Proses ini memastikan integritas data dan meningkatkan keamanan aplikasi dari potensi input yang tidak diinginkan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF Token diperlukan saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), di mana penyerang dapat memanipulasi pengguna untuk mengirimkan permintaan tidak sah ke server. Tanpa CSRF Token, form menjadi rentan terhadap serangan tersebut, yang memungkinkan penyerang membuat permintaan yang tidak diinginkan atas nama pengguna yang sudah login. Hal ini dapat digunakan untuk mengubah data sensitif atau melakukan tindakan yang merugikan. Dengan menyertakan CSRF Token, aplikasi dapat memastikan bahwa setiap permintaan yang diterima adalah sah dan berasal dari pengguna yang terautentikasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- Membuat Direktori Templates dan File HTML
Mempersiapkan struktur dasar tampilan aplikasi web dengan membuat direktori templates dan file base.html untuk kerangka halaman yang konsisten.
- Konfigurasi settings.py dan Menyusun main.html
Mengatur Django untuk mengenali direktori template melalui settings.py, kemudian menggunakan {% extends 'base.html' %} pada main.html untuk menampilkan konten spesifik pada halaman.
- Menyiapkan Model dan Melakukan Migrasi
Membuat model data di models.py, melakukan migrasi untuk memperbarui skema database, dan memungkinkan penyimpanan data produk.
- Membuat Form Input Data dan Menampilkan Item di HTML
Membuat ProductForm di forms.py untuk menangkap input data produk dari pengguna, mengintegrasikannya ke dalam views.py, serta menampilkan dan memvalidasi form di create_product.html.
- Mengembalikan Data dalam Format XML
Menambahkan fungsi di views.py untuk mengubah data produk menjadi format XML dan mengaksesnya melalui browser.
- Mengembalikan Data dalam Format JSON
Membuat fungsi serupa untuk mengubah data menjadi format JSON dan mengaksesnya di browser.
- Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON
Menambahkan fungsi untuk menampilkan data produk berdasarkan ID dalam format XML dan JSON, serta memperbarui URL untuk aksesnya.
- Menggunakan Postman untuk Menguji API
Menggunakan Postman untuk menguji pengambilan data melalui API dengan format XML dan JSON, serta menguji pengambilan data berdasarkan ID.
- Deployment Otomatis ke PWS Menggunakan GitHub Actions
Menyiapkan GitHub Actions untuk otomatisasi deployment ke PWS setiap kali melakukan push ke branch utama di GitHub, dengan menambahkan file konfigurasi deploy.yml.

<img width="1440" alt="Screenshot 2024-09-18 at 11 08 43" src="https://github.com/user-attachments/assets/a63137b9-2d79-43a3-bf0b-e1c89101ed01">
<img width="1440" alt="Screenshot 2024-09-18 at 11 08 22" src="https://github.com/user-attachments/assets/f1b07d8a-a2b1-4016-a4a3-aa13db2c6d45">
<img width="1440" alt="Screenshot 2024-09-18 at 11 08 03" src="https://github.com/user-attachments/assets/a4ed5733-a874-42d7-a8af-2530ce907aab">
<img width="1440" alt="Screenshot 2024-09-18 at 11 07 33" src="https://github.com/user-attachments/assets/963b3647-2a46-4b26-9e22-bf77d3946ed0">
<img width="1440" alt="Screenshot 2024-09-18 at 11 08 43" src="https://github.com/user-attachments/assets/5c1fd93b-5c3f-4a29-b23e-d40f8b6434d3">

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
TUGAS 4

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
- Dalam hal fleksibelitas, redirect() lebih fleksibel karena bisa menerima URL sebagai string, nama URL, atau objek model. Sedangkan HttpResponseRedirect() hanya menerima string URL.
- Redirect() sering kali lebih terintegrasi dengan middleware Django, sehingga lebih mudah digunakan dalam konteks yang melibatkan autentikasi dan otorisasi.

2. Jelaskan cara kerja penghubungan model Product dengan User!
Hubungan antara model Product dan model User di Django umumnya dilakukan melalui relasi ForeignKey, di mana setiap produk dimiliki oleh satu pengguna. Model Product memiliki atribut owner yang menyimpan ID pengguna yang menciptakan produk tersebut. Ini memungkinkan pengaitannya dengan pengguna dan melakukan query untuk menampilkan semua produk yang dimiliki oleh pengguna tersebut. 

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses memverifikasi identitas pengguna, biasanya dengan memeriksa username dan password, sedangkan authorization adalah proses yang menentukan apakah pengguna yang sudah terautentikasi memiliki izin untuk mengakses atau melakukan tindakan tertentu.

Ketika pengguna login, sistem pertama-tama memeriksa kredensial mereka (authentication), dan jika berhasil, pengguna diberi akses ke berbagai fitur berdasarkan hak yang dimiliki (authorization). Django mengimplementasikan authentication melalui fungsi authenticate() untuk memverifikasi pengguna, dan login() untuk memulai sesi. Django juga menyediakan decorator @login_required untuk memastikan bahwa hanya pengguna yang sudah terautentikasi yang dapat mengakses halaman atau fungsi tertentu.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login melalui sistem sesi dan cookie. Saat login berhasil, Django membuat sesi di server dan menyimpan ID sesi dalam cookie di browser pengguna. Setiap kali pengguna melakukan permintaan, Django membaca cookie untuk mendapatkan ID sesi dan mencocokkannya dengan data sesi di server, yang berisi informasi pengguna dan status autentikasi. Middleware sesi Django secara otomatis mengelola penyimpanan dan penghapusan data sesi, sehingga pengguna tetap terhubung saat menjelajah aplikasi, selama sesi masih aktif atau hingga mereka logout.

Cookies digunakan untuk mengingat pengguna, menyimpan preferensi, dan melacak aktivitas. Namun, tidak semua cookies aman, mereka dapat menjadi target serangan jika tidak dikelola dengan benar. Penting untuk menggunakan fitur keamanan seperti HttpOnly dan Secure, serta memberi pengguna kontrol atas pengaturan privasi mereka.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Fungsi dan Formulir Registrasi: Buat fungsi dan halaman registrasi dengan mengimpor UserCreationForm dan message dari django.contrib.auth. UserCreationForm mempermudah pembuatan formulir pendaftaran. Tambahkan fungsi registrasi untuk menghasilkan formulir dan membuat akun pengguna saat disubmit. Buat file HTML untuk halaman pendaftaran yang mengumpulkan data dengan aman dan memberikan umpan balik pendaftaran melalui sistem pesan. Impor fungsi registrasi di views.py dan tambahkan path URL ke urlpatterns.
- Fungsi Login: Tambahkan beberapa impor seperti authenticate, login, dan AuthenticationForm untuk mengimplementasikan fungsi login. Buat fungsi login_user di views.py yang mengautentikasi pengguna dan membuat sesi untuk pengguna yang valid. Buat file baru login.html sebagai template untuk login dan opsi pendaftaran bagi pengguna baru.
Restriksi Akses Halaman Utama: Tambahkan login_required untuk memastikan pengguna harus login sebelum mengakses halaman utama. Gunakan dekorator @login_required(login_url='/login') pada halaman utama dan jalankan proyek Django di http://localhost:8000/.
- Penggunaan Cookies: Tambahkan cookie untuk menyimpan data login terakhir dan tampilkan di halaman utama. Impor fungsi seperti HttpResponseRedirect, reverse, dan datetime di views.py. Tambahkan cookie last_login pada respons untuk menampilkan informasi terakhir login. Ubah fungsi logout_user untuk menghapus cookie saat logout, dan tampilkan pesan mengenai sesi terakhir login.
- Melihat Cookie: Untuk melihat cookie, buka protokol localhost di Chrome, klik kanan pada halaman web, pilih "Inspect," lalu navigasi ke tab "Application" untuk melihat cookie yang ada.
- Menghubungkan Model Entry dengan User: Tambahkan impor di models.py untuk membuat relasi antara model dan pengguna. Buat variabel user guna mengaitkan setiap entri produk dengan pengguna. Di views.py, gunakan parameter commit=False untuk menunda penyimpanan objek ke database, kemudian ubah kode untuk menampilkan entri produk yang terkait dengan pengguna yang sedang login. Setelah itu, simpan perubahan, lakukan migrasi, dan atasi error dengan menetapkan nilai default untuk field user pada semua entri yang ada. Terakhir, impor os dan sesuaikan variabel DEBUG sesuai kebutuhan.
- Lalu lakukan Deploy ke PWS
- Pada web Covela, klik register untuk menambahkan akun (untuk ketentuan tugas maka perlu dibuat 2 akun). Selanjutnya tambahkan tiga Product pada web tersebut.












