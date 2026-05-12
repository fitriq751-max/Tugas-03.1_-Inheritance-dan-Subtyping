**IDENTITAS MAHASISWA**
* **Nama** : Fitri Khairani Sitorus
* **NIM** : 12550120344
* **Prodi** : Teknik Informatika
* **Kampus**: UIN Suska Riau
* **Tugas** : 03.1 - Inheritance dan Subtyping


# 💰 SMART PAYROLL: Sistem Penggajian Karyawan

Aplikasi ini adalah sistem manajemen data pegawai dan perhitungan gaji otomatis yang dibangun menggunakan konsep Pemrograman Berorientasi Objek (OOP) dengan bahasa pemrograman Python. 

## 🚀 Fitur Utama
* **Hitung Gaji Otomatis**: Sekali klik, sistem langsung tahu cara menghitung gaji yang berbeda-beda untuk tiap jabatan (Staff, Manajer, Supervisor, atau AdminHRD).
* **Input Karyawan Baru**: Kita bisa memasukkan data orang baru secara langsung ke dalam sistem kantor dengan pilihan jabatan yang lengkap.
* **Slip Gaji Rapi**: Menampilkan rincian gaji dalam bentuk tabel yang bagus, bersih, dan gampang dibaca.
* **Cek Kas Kantor**: Menghitung total keseluruhan uang yang harus disiapkan kantor untuk membayar semua gaji karyawan.

## 🏗️ Konsep OOP yang Diterapkan
1. **Inheritance (Pewarisan)**: Menggunakan hirarki kelas (Pegawai -> Staff -> Manajer) untuk menurunkan sifat dan metode.
2. **super() Function**: Digunakan untuk memanggil metode dari kelas induk agar struktur kode lebih efisien.
3. **Subtyping**: Mengelola berbagai tipe objek jabatan dalam satu daftar (list) perusahaan yang terintegrasi.
4. **Abstraction**: Menggunakan kelas abstrak (ABC) untuk memastikan setiap entitas pegawai memiliki kerangka yang konsisten.

## 📁 Struktur File Proyek
* `pegawai.py`: Kelas induk (Abstract Class) untuk identitas dasar.
* `jabatan.py`: Berisi kelas-kelas jabatan (Staff, Manajer, Supervisor, AdminHRD).
* `perusahaan.py`: Logika pengelola koleksi data seluruh pegawai.
* `main.py`: Program utama untuk demo sistem.
* `main_interaktif.py`: Program utama dengan fitur input data langsung.

## 🛠️ Cara Menjalankan
1. Pastikan Python sudah terinstal.
2. Instal library pendukung:
   ```bash
   pip install rich pyfiglet
