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

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
TUGAS 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Dalam CSS, urutan prioritas penentuan selector dimulai dari yang tertinggi, yaitu gaya inline (style langsung pada elemen), diikuti oleh selector ID, lalu class, atribut, dan pseudo-class, kemudian selector tipe elemen dan pseudo-element. Jika terdapat properti dengan !important, properti tersebut akan diutamakan, meskipun spesifisitasnya lebih rendah. Jika dua selector memiliki tingkat spesifisitas yang sama, aturan yang muncul terakhir dalam urutan sumber (cascade) akan diutamakan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting dalam pengembangan aplikasi web karena memastikan situs dapat menyesuaikan tampilan dan fungsinya sesuai dengan berbagai ukuran layar dan perangkat yang digunakan. Dengan semakin banyaknya pengguna yang mengakses situs melalui perangkat mobile seperti smartphone dan tablet, situs web perlu terlihat baik di layar kecil maupun besar. Responsive design memberikan pengalaman yang konsisten dalam hal navigasi dan kenyamanan pengguna, tanpa perlu membuat versi situs yang berbeda untuk setiap perangkat.

- Aplikasi yang sudah menerapkan responsive design : Twitter, Instagram, Spotify, Netflix, LinkedIn, YouTube, Canva
- Aplikasi yang belum menerapkan responsive design : Craigslist, KAI Access (versi lama), MTV.com

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin, border, dan padding adalah tiga properti CSS yang digunakan untuk mengatur tata letak elemen HTML. Margin adalah ruang di luar border yang menentukan jarak antara elemen dengan elemen lain di sekitarnya, border adalah garis yang mengelilingi elemen di antara margin dan padding, sementara padding adalah ruang antara konten elemen dan tepi dalam elemen. Padding mengatur jarak konten dengan batas elemen, border memberikan garis pemisah di sekitar elemen, dan margin memastikan elemen tidak bersinggungan dengan elemen lain di halaman. Ketiganya dapat diatur untuk setiap sisi elemen secara spesifik untuk mencapai desain yang diinginkan.

- Contoh implementasi margin : 
.container {
    padding-top: 10px;
    padding-right: 15px;
    padding-bottom: 10px;
    padding-left: 15px;
}

- Contoh implementasi border : 
.container {
    border-top: 2px solid red;
    border-right: 2px dashed green;
    border-bottom: 2px dotted blue;
    border-left: 2px solid black;
}

- Contoh implementasi padding :
.container {
    padding-top: 10px;
    padding-right: 15px;
    padding-bottom: 10px;
    padding-left: 15px;
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah sistem satu dimensi yang ideal untuk menyusun elemen secara horizontal atau vertikal, dengan fleksibilitas dalam mengatur jarak antar elemen dan membuat tata letak yang responsif. Ini sangat cocok untuk tata letak yang lebih sederhana, seperti menu atau elemen yang disusun dalam satu baris atau kolom. Grid Layout adalah sistem dua dimensi yang memungkinkan penyusunan elemen dalam baris dan kolom secara bersamaan, memberikan kontrol yang lebih besar atas posisi dan ukuran elemen, sehingga sangat cocok untuk tata letak yang lebih kompleks seperti dashboard atau galeri. Keduanya membantu membuat tata letak yang dinamis dan responsif, tetapi Flexbox digunakan untuk tata letak satu dimensi, sementara Grid lebih baik untuk tata letak dua dimensi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Integrasi Tailwind CSS: Pertama, buka project Django Anda dan edit file base.html. Tambahkan tag <meta name="viewport"> untuk memastikan tampilan responsif. Kemudian, hubungkan template Django dengan Tailwind CSS menggunakan skrip CDN dengan menambahkan kode tersebut di dalam file base.html.
- Menambahkan Fitur Edit Product: Buka file views.py dan buat fungsi baru untuk fitur edit produk. Jangan lupa untuk menambahkan import yang relevan. Selanjutnya, buka file edit_product.html dan sesuaikan isinya. Di urls.py, tambahkan path URL dan import yang diperlukan, serta pastikan URL menuju fitur edit menggunakan {% url 'main:edit_product' product_entry.pk %}.
- Menambahkan Fitur Hapus Mood: Buat fungsi baru bernama delete_mood di views.py, kemudian tambahkan path URL dan import yang sesuai di urls.py. Setelah itu, buka file main.html dan tambahkan URL untuk menghapus mood dengan benar.
- Menambahkan Navigation Bar: Buat file navbar.html di dalam folder templates yang sejajar dengan main.html. Kaitkan file main.html, create_product_entry.html, dan edit_product.html dengan menambahkan elemen navigasi yang mengarah ke halaman-halaman tersebut.
- Konfigurasi Static Files: Pada file settings.py, tambahkan 'whitenoise.middleware.WhiteNoiseMiddleware'untuk menangani file statis. Pastikan variabel seperti STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL dikonfigurasi dengan benar untuk mengelola file CSS dan gambar.
- Menambahkan Gambar dan Styling (Opsional): Jika ingin menambahkan gambar, impor gambar tersebut ke dalam folder static, yang biasanya berisi folder css dan images. Hubungkan file global.css dan Tailwind CSS ke base.html, kemudian tambahkan custom styling di global.css. Lakukan styling pada halaman login, register.html, dan buat juga halaman card_product.html di folder templates. Jangan lupa untuk memberikan gaya pada halaman create_product_entry.html dan edit_product.html agar tampilan lebih menarik.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
TUGAS 6

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
- Interaktivitas Tinggi
JavaScript memungkinkan pembuatan tampilan dinamis pada sebuah website. Contohnya, membuat efek animasi, dropdown menus, slideshow, dan fitur-fitur lain yang memudahkan pengguna dalam berinteraksi dengan halaman web.
- Validasi Formulir dan Input
JavaScript dapat digunakan untuk memvalidasi formulir di website. Ini memastikan bahwa pengguna telah memasukkan data yang benar dan lengkap sebelum mengirimkan formulir, meningkatkan keakuratan data yang diterima.
- Animasi dan Efek Visual
JavaScript sangat efektif dalam membuat animasi dan efek visual menarik pada halaman web. Contohnya adalah slideshow, menu drop-down, animasi tombol, dan efek hover, yang meningkatkan daya tarik visual situs.
- Manipulasi HTML dan CSS
JavaScript memungkinkan pengembang untuk mengakses dan memanipulasi struktur halaman web melalui DOM (Document Object Model). Ini memungkinkan pengembang untuk menambahkan, menghapus, atau mengubah elemen-elemen HTML dan CSS secara dinamis, memberikan fleksibilitas tinggi dalam pengembangan.
- Respons Instan Terhadap Aksi Pengguna**
Dengan JavaScript, pengembang dapat memberikan respons instan kepada pengguna setelah mereka melakukan aksi tertentu, seperti mengklik tombol atau mengisi formulir. Hal ini secara signifikan meningkatkan pengalaman pengguna di situs web.
- Integrasi dengan Framework dan Library
JavaScript memiliki banyak framework dan library yang membantu mempercepat dan mempermudah proses pengembangan aplikasi web. Framework seperti React, Angular, dan Vue.js memungkinkan pengembangan aplikasi web secara cepat dan efisien.
- Kecepatan Loading Website
Kecepatan loading website adalah faktor penting dalam peringkat SEO. Penggunaan JavaScript yang optimal dapat membantu meningkatkan performa loading website, yang berpengaruh pada peringkat website di mesin pencari seperti Google.
- Fleksibilitas Penerapan
Walaupun awalnya digunakan di frontend, implementasi JavaScript telah berkembang ke backend dengan adanya Node.js. Hal ini memungkinkan pengembang untuk mengelola server dan database menggunakan JavaScript, memberikan fleksibilitas penuh dalam pengembangan aplikasi web.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

Penggunaan `await` ketika menggunakan `fetch()` memiliki beberapa tujuan utama yang sangat berguna dalam pengembangan aplikasi web asinkron. 
Fungsi dari `await` adalah untuk menunggu sampai promse (Promise) selesai sebelum melanjutkan eksekusi kode. Ketika Anda menggunakan `await` dengan `fetch()`, kita membiarkan JavaScript menunggu hingga permintaan HTTP selesai dan respons datanya tersedia sebelum melanjutkan ke langkah berikutnya. 

Contoh penggunaan `await` dengan `fetch()` adalah sebagai berikut: 

```async function getProductEntries(){
      	 return fetch("{% url 'main:show_json' %}").then((res) => res.json())
```

Dalam contoh ini, `await` digunakan untuk menunggu sampai `fetch(url)` selesai dan respons textnya tersedia sebelum mengembalikan hasilnya.
Await membuat kode yang asinkron berperilaku seperti kode yang sinkron, sehingga akan lebih mudah untuk dibaca dan dipahami. Dengan await, kita dapat menghindari penggunaan callback yang ebrtumpuk, sehingga kode akan lebih bersih dan terstruktur.

Jika kita tidak menggunakan `await`, kita harus menggunakan `.then()` untuk menangani hasil promse. Cara ini sering disebut sebagai "callback hell," karena dapat membuat kode menjadi rumit dan sulit dibaca. 

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Penggunaan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST sangat penting dalam konteks keamanan aplikasi web yang dibangun dengan Django. Berikut adalah alasan-alasan mengapa kita perlu menggunakan decorator ini dan apa yang terjadi jika kita tidak menggunakannya.

Alasan Menggunakan `csrf_exempt` :
- Menghindari Pengecekan CSRF**
Dekorator `csrf_exempt` menandai view tertentu agar tidak diperiksa oleh middleware CSRF. Ini berguna ketika kita melakukan permintaan POST melalui AJAX, di mana pengiriman token CSRF mungkin tidak selalu dilakukan atau sulit untuk diatur dalam konteks JavaScript.
- Kemudahan dalam Pengembangan**
Dalam banyak kasus, terutama saat mengembangkan aplikasi dengan banyak interaksi AJAX, menggunakan `csrf_exempt` dapat menyederhanakan proses pengembangan. Pengembang tidak perlu khawatir tentang pengaturan token CSRF untuk setiap permintaan POST yang dilakukan melalui AJAX.
- Fleksibilitas**
Dengan menandai view tertentu sebagai exempt dari pemeriksaan CSRF, kita memberikan fleksibilitas dalam menangani permintaan yang mungkin tidak memerlukan perlindungan CSRF, seperti permintaan dari API yang diakses oleh klien tepercaya.

Apa Yang Terjadi Jika Tidak Menggunakan `csrf_exempt`:
- Error 403 Forbidden
Jika kita tidak menggunakan `csrf_exempt` dan juga tidak mengirimkan token CSRF dengan benar dalam permintaan AJAX, server akan menolak permintaan tersebut dan mengembalikan error 403 Forbidden. Ini terjadi karena Django secara otomatis memeriksa keberadaan token CSRF untuk semua permintaan POST.
- Kerumitan Penanganan Token
Tanpa `csrf_exempt`, kita harus memastikan bahwa setiap permintaan AJAX menyertakan token CSRF yang valid. Ini bisa menjadi rumit, terutama jika ada banyak permintaan AJAX yang dilakukan dari sisi klien dan setiap permintaan harus menangani token dengan cara yang benar.
- Potensi Kerentanan Keamanan
Jika kita mengabaikan perlindungan CSRF pada view yang seharusnya dilindungi, tanpa menggunakan `csrf_exempt`, maka kita berisiko membuka celah keamanan di aplikasi kita. Namun, jika kita menggunakan `csrf_exempt` pada view yang seharusnya tetap aman, maka ini juga dapat menyebabkan kerentanan terhadap serangan CSRF.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Keamanan Data :
- Melawan Serangan Cross-Site Scripting (XSS) : Jika pembersihan data dilakukan di frontend, maka data yang tidak bersih dapat dieksploitasi oleh serangan XSS. Oleh karena itu, melakukan pembersihan di backend membantu melindungi data dari serangan ini.
- Menyaring Masukan Malicious : Di backend, kita dapat lebih efektif dalam menyaring masukan malicious yang mungkin dicoba oleh pengguna untuk merugikan aplikasi.

Stabilitas Sistem :
- Menghindari Ketergantungan Browser : Jika pembersihan dilakukan di browser, maka kinerja aplikasi dapat dipengaruhi oleh varietas browser yang berbeda-beda. Di backend, kita dapat memastikan bahwa pembersihan dilakukan secara konsisten tanpa ketergantungan pada teknologi front-end.
- Otomatisasi Prosess : Backend memungkinkan kita untuk membuat proses pembersihan data menjadi otomatis, sehingga tidak perlu repot-repot melakukan manual check-up setiap kali user input.

Skalabilitas dan Integrasi :
- Scalability : Saat aplikasi berkembang, backend lebih mudah skalabel dibandingkan dengan frontend. Artinya, kita dapat menambahkan lebih banyak resources untuk memproses data tanpa mempengaruhi performance aplikasi secara signifikan.
- Integration with Other Services : Backend seringkali berintegrasi dengan services lain seperti databases, APIs, dll., sehingga melakukan pembersihan di sana memungkinkan integrasi yang lebih baik dan koheren.

Transparency dan Audit Trail :
- Audit Trail : Dengan melakukan pembersihan di backend, kita dapat menciptakan trail audit yang lebih transparan tentang apa yang telah dilakukan pada data pengguna. Ini sangat penting untuk tujuan legal dan compliance.
- Logging Activity : Logging activity related to data cleaning can provide valuable insights into how the system handles different types of inputs which helps in improving overall security posture.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

**Menambahkan Error Message Pada Login**
- Untuk memudahkan proses login pada aplikasi, berikan conditional pada view login_user
  ```
    messages.error(request, msg)
  ```
    pesan ini akan "menempelkan" pesan error kepada request yang mengirimkan permintaan login, yang nantinya akan ditampilkan di templat login.html

**Membuat Fungsi untuk Menambahkan Product dengan AJAX**

- Tambahkan kedua import berikut
   ```
      from django.views.decorators.csrf import csrf_exempt
   ```
   ```
    from django.views.decorators.http import require_POST pada file views.py
   ```

- Buat fungsi baru pada views.py dengan nama add_product_entry_ajax yang menerima parameter request
    ```
      name = request.POST.get(“name”)
    ```
  digunakan untuk mengambil data yang dikirimkan pengguna melalui POST request secara manual.
    ```
      new_product = Product(…)
    ```
  merupakan objek Product baru yang dibuat secara manual berdasarkan data-data yang dikirimkan dari POST request.

**Menambahkan Routing Untuk Fungsi add_product_entry_ajax**

- Buka urls.py yang ada pada subdirektori main dan impor fungsi yang sudah  dibuat tadi dan tambahkan path url ke dalam urlpatterns
   untuk mengakses fungsi yang sudah diimpor.

**Menampilkan Data Product Entry dengan fetch() API**

- Pada berkas views.py hapus dua baris berikut:
    ```
      product_entries = Product.objects.filter(user=request.user)
    ```
    ```
      'product_entries': product_entries,
    ```
Akan didapatkan objek-objek product entry dari endpoint /json, sehingga kode di atas tidak diperlukan lagi.

- Pada berkas views.py dan ubah baris pertama views untuk show_json dan show_xml seperti berikut :
    ```
      data = Product.objects.filter(user=request.user)
    ```

- Pada berkas main.html hapus bagian block conditional product_entries untuk menampilkan card_product ketika kosong
  atau tidak lalu ditambahkan potongan kode ini di tempat yang sama
    ```
      div dengan id=“product_entry_cards"
    ```

- Buat block script di bagian bawah berkas main.html (sebelum {% endblock content %}) dan buatlah fungsi baru pada block script tersebut dengan nama getProductEntries.

Fungsi ini menggunakan fetch() API ke data JSON secara asynchronous.
Setelah data di-fetch, fungsi then() digunakan untuk melakukan parse pada data JSON menjadi objek JavaScript.

- Buatlah fungsi baru pada block script dengan nama refreshProductEntries yang digunakan untuk me-refresh data products secara asinkronus.
    ```
      document.getElementById(“product_entry_cards")
    ```
digunakan untuk mendapatkan elemen berdasarkan ID nya. Pada baris kode ini, elemen yang dituju adalah tag dengan ID product_entry_cards yang sudah kamu buat pada tahapan sebelumnya.
    ```
      innerHTML
    ```
digunakan untuk mengisi child element dari elemen yang dituju. Jika innerHTML = "", maka akan mengosongkan isi child element dari elemen yang dituju.
    ```
      className
    ```
digunakan untuk mengisi class name dari elemen yang dituju.
    ```
      productEntries.forEach((item))
    ```
digunakan untuk melakukan for each loop pada data moods yang diambil menggunakan fungsi getProductEntries(). Kemudian, htmlString kita konkatenasi dengan data moods untuk   mengisi container dengan cards seperti pada tutorial sebelumnya.
    ```
      refreshProductEntries()
    ```
digunakan untuk memanggil fungsi tersebut pada setiap kali membuka halaman web.

**Membuat Modal Sebagai Form untuk Menambahkan Product**

- Tambahkan kode form untuk mengimplementasikan modal (Tailwind) pada aplikasi. Potongan kode form diletakan di bawah div dengan id product_entry_cards yang telah ditambahkan sebelumnya.

- Agar modal dapat berfungsi, perlu ditambahkan fungsi-fungsi JavaScript berikut.
    ```
      function showModal()
    ```
    ```
      function hideModal()
    ```
- Tambahkan tombol baru untuk melakukan penambahan data dengan AJAX.

**Menambahkan Data Product dengan AJAX**

Modal dengan form yang telah dibuat sebelumnya belum bisa digunakan untuk menambahkan data product. Oleh karena itu, perlu dibuat fungsi JavaScript baru untuk menambahkan data berdasarkan input ke basis data secara AJAX.

- Buat fungsi baru pada block script dengan nama addProductEntry
    ```
      new FormData(document.querySelector(‘#productEntryForm'))
    ```
digunakan untuk membuat sebuah FormData baru yang datanya diambil dari form pada modal. Objek FormData dapat digunakan untuk mengirimkan data form tersebut ke server.
    ```
      document.getElementById(“productEntryForm").reset()
    ```
digunakan untuk mengosongkan isi field form modal setelah di-submit.
    
- Tambahkan sebuah event listener pada form yang ada di modal untuk menjalankan fungsi addProductEntry()

**Melindungi Aplikasi dari Cross Site Scripting (XSS)**

- Menambahkan strip_tags untuk "Membersihkan" Data Baru dengan buka berkas views.py dan forms.py dan tambahkan impor berikut :
      ```
        from django.utils.html import strip_tags
      ```
- Pada fungsi add_product_entry_ajax di views.py, gunakanlah fungsi strip_tags pada data name dan description dan pairing sebelum data tersebut dimasukkan ke dalam Product
    
- Pada class ProductEntryForm di forms.py tambahkan ketiga method berikut :
    ```
      clean_name()
    ```
    ```
      clean_description()
    ```
    ```
      clean_pairing()
    ```
  
Method clean_name dan clean_description dan clean_pairing akan dipanggil ketika melakukan form.is_valid(), sehingga dengan menambahkan kedua method tersebut sudah melakukan validasi untuk fungsi create_product dan edit_product.

**Membersihkan Data dengan DOMPurify**

    Bisa menggunakan library JavaScript DOMPurify untuk melakukan pembersihan di frontend.
    
- Buka berkas main.html dan tambahkan potongan kode berikut pada block meta dalam block script
    ```
      src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js">
    ```
    
- Pada fungsi refreshProductEntries yang telah ditambahkan sebelumnya, tambahkan potongan kode berikut.
    ```
      const name = DOMPurify.sanitize(item.fields.name);
    ```
    ```
      const description = DOMPurify.sanitize(item.fields.description);
    ```
    ```
      const pairing = DOMPurify.sanitize(item.fields.pairing);
    ```
    
- Refresh halaman utama dan jika sebelumnya memiliki data yang "kotor" seperti yang memunculkan alert box, seharusnya tidak muncul lagi.
















