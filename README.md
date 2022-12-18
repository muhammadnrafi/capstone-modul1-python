# YP Directory - Data Kontak Telepon Python Program
## Capstone Project Module 1 - Python Programming
### Purwadhika JCDS 1904 By Muhammad Naufal Rafi

Capstone Project adalah sebuah projek akhir pada tiap module pembelajaran yang telah diberikan kepada peserta program untuk mengukur seberapa jauh pemahaman peserta terhadap materi dengan langsung mengaplikasikannya ke dalam suatu mini aplikasi.
Dalam pengerjaan project ini tiap peserta diwajibkan untuk membuat 4 fitur utama yang terdiri dari: *Create*, *Read*, *Update*, dan *Delete* pada masing masing program.

Topik yang saya kerjakan adalah sebuah program yang dapat memuat Data Kontak Telepon seperti hal-nya *YellowPages*. Jadi *YellowPages*
adalah sebuah direktori yang berisi informasi telepon bisnis, industri dan layanan jasa. 
Pada projek ini saya membuat sebuah program yang bernama **YP Directory**, yang dapat menampilkan direktori kontak telepon dari berbagai perusahaan sehingga dalam projek ini nomor telepon digunakan sebagai unique code dalam data yang digunakan.
Berikut adalah penjelasan lebih lanjut dari program tersebut:

![capstone_1](https://user-images.githubusercontent.com/116897129/208296983-aaf87472-2660-49fe-ace8-4ac0e8ed88a5.PNG)
![capstone_2](https://user-images.githubusercontent.com/116897129/208297403-5c4b6f3a-2ed7-404c-9132-252775945b80.PNG)
![capstone_3](https://user-images.githubusercontent.com/116897129/208297428-3a6be10f-fa0d-46a7-8b30-cd9faa28d7a7.PNG)
1. Pada Menu Awal YP Directory terdapat 3 pilihan menu yaitu Menu Admin, Menu Pembaca dan Keluar Program.
Pada menu ini terdapat perbedaan antara menu admin dan menu pembaca, untuk menu admin sendiri dibuat untuk admin dari YP Directory yang dapat me-*manage* isi dari program tersebut seperti menambah, mengubah, serta menghapus data, sedangkan pada menu pembaca hanya dapat membaca isi data dari direktori nomor telepon.
Untuk dapat mengakses Menu Admin diperlukan sebuah akses kode pass: 12345 yang sebelumnya sudah didefinisikan, selanjutnya ada menu pembaca yang dapat diakses tanpa menggunakan kode pass, dan yang terakhir adalah keluar program untuk mengakhiri program.


![capstone_5](https://user-images.githubusercontent.com/116897129/208297666-85277cbd-924f-4d5a-9e6a-b51c664a9dd9.PNG)
![capstone_6](https://user-images.githubusercontent.com/116897129/208297667-c03a093d-58f4-4c63-b29c-9eac007763c8.PNG)
![capstone_7](https://user-images.githubusercontent.com/116897129/208297664-d8ac8f0f-eb22-4629-a822-428beb7fa4f2.PNG)

2. Pada menu menampilkan data dapat diakses dengan memilih input menu pembaca dan juga menu admin, pada menu ini dapat menampilkan data direktori nomor telepon secara kesuluruhan, berdasarkan kategori maupun dengan menggunakan fitur pencarian berdasarkan kata kunci.

![capstone_8](https://user-images.githubusercontent.com/116897129/208297752-58cd92a0-5780-47f1-97a7-f6cc8d2557d7.PNG)

3. Untuk keluar dari halaman menampilkan data, ke menu sebelumnya dapat memilih pilihan 4 pada menu namun perlu di ingat ketika sebelumnya mengakses menu menampilkan data dari menu admin maka perlu melakukan input kode pass kembali.
Jika kode pass yang dimasukkan salah maka user tidak dapat mengakses menu admin kembali dan langsung keluar ke menu awal.


![capstone_9](https://user-images.githubusercontent.com/116897129/208297895-8248760e-0f65-461f-8eb8-95669f30b15a.PNG)

4. Selanjutnya adalah fitur untuk menambahkan data. Fitur ini hanya dapat diakses oleh admin dari YP Directory sehingga tidak semua orang dapat memiliki akses. 
Dalam fitur ini user dapat melakukan input data dengan syarat unique code tiap data harus berbeda.

![capstone_10](https://user-images.githubusercontent.com/116897129/208298023-099c4b89-6bfa-4ae3-baae-b37c2cc1335c.PNG)

5. Untuk fitur update, user dapat melakukan perubahan terhadap data di direktori dengan memasukkan unique code dalam hal ini nomor telepon
jika nomor telepon yang dimasukkan tidak ditemukan maka fitur update tidak akan bekerja, dan jika terdapat nomor telepon yang dimaksud maka user dapat melakukan perubahan terhadap data di direktori seperti mengubah nama, kategori, nomor telepon, kota, alamat, serta email/web.

![capstone_11](https://user-images.githubusercontent.com/116897129/208298129-3d69d920-a94d-4895-b6a9-eee4f166570f.PNG)

6. Fitur Hapus, berfungsi untuk menghapus isi data dari direktori. Pada fitur ini terdapat 2 pilihan yaitu hanya data tertentu berdasarkan nomor telepon dan hapus keseluruhan data. Jika data telah dihapus maka data tersebut tidak akan muncul kembali di direktori.



![capstone_14](https://user-images.githubusercontent.com/116897129/208298234-1e716587-e2fa-4c21-9077-2a837ac4836c.PNG)

7. Ketika Program telah selesai digunakan user dapat melakukan exit program pada menu awal, jika user berada pada sub menu admin/pembaca maka user dapat keluar dari halaman tersebut dengan memilih opsi kembali ke halaman sebelumnya. 
