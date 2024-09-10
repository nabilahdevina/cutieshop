Nama : Nabilah Devina Mumin

NPM : 2306245876

Kelas : PBP B 

1.⁠ ⁠Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

•⁠  ⁠Pertama-tama, kita buat proyek Django baru dengan nama "cutieshop". Proyek ini adalah kerangka kerja utama yang akan mengatur aplikasi dan pengaturannya. Pastikan proyek ini berada dalam direktori utama bernama "cutieshop" dan terhubung dengan repositori GitHub. Ini berfungsi untuk menyimpan kode di GitHub dan memantau perubahan yang dibuat.
•⁠  ⁠Selanjutnya, kita buat aplikasi baru di dalam proyek Django ini. Kita beri nama aplikasi ini "main".
•⁠  ⁠Agar aplikasi "main" dikenali oleh proyek "cutieshop", kita perlu mendaftarkannya. Buka file settings.py di proyek dan tambahkan nama "main" ke dalam daftar INSTALLED_APPS.
•⁠  ⁠Sekarang kita perlu mendefinisikan struktur data yang akan digunakan aplikasi. Buka file models.py di aplikasi "main" dan buat class bernama Product. Fungsi models.py adalah untuk menyimpan script database.
•⁠  ⁠Buat folder baru dengan nama "templates" di dalam direktori aplikasi "main". Di dalam folder ini, buat file HTML bernama "main.html". File ini akan digunakan untuk mendefinisikan bagaimana data dari aplikasi ditampilkan kepada pengguna di halaman web.
•⁠  ⁠Buka file views.py dan tambahkan fungsi yang akan menghubungkan data dari model dengan template HTML yang kita buat. Fungsi ini akan mengambil data produk dan mengirimkannya ke template "main.html" untuk ditampilkan. Ini adalah cara aplikasi menunjukkan informasi kepada pengguna.
-  Di dalam aplikasi "main", buat file urls.py untuk mengatur URL yang akan mengarahkan pengguna ke tampilan yang tepat. 
•⁠  ⁠Buka file urls.py di proyek "cutieshop" dan tambahkan rute yang mengarah ke file urls.py di aplikasi "main".
•⁠  ⁠Setelah semuanya siap, saatnya untuk Deployment ke PWS.

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
