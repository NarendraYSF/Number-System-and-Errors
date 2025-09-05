# 🔢 GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan

Aplikasi GUI yang menyediakan antarmuka grafis untuk Simulator Sistem Bilangan dengan kemampuan konversi antar sistem, operasi aritmatika, simulasi kesalahan, dan deteksi kesalahan.

## 🚀 Cara Menjalankan

### 1. GUI Standar
```bash
python gui_simulator.py
```

### 2. GUI dengan Demo
```bash
python demo_gui.py
```

### 3. CLI (Command Line Interface)
```bash
python number_system_simulator.py
```

### 4. Test Suite
```bash
python test_simulator.py
```

## 📋 Fitur GUI

### 🔄 Tab Konversi
- **Konversi Antar Sistem**: Konversi nilai dari satu sistem bilangan ke sistem lainnya
- **Tabel Lengkap**: Menampilkan konversi ke semua sistem bilangan sekaligus
- **Validasi Input**: Memastikan input sesuai dengan sistem bilangan yang dipilih
- **Riwayat Otomatis**: Semua konversi tersimpan dalam riwayat

### 🧮 Tab Aritmatika
- **Operasi Dasar**: Penjumlahan (+), Pengurangan (-), Perkalian (*)
- **Operasi Lanjutan**: Pembagian (/), Modulo (%), Pangkat (**)
- **Multi-Sistem**: Operasi dalam biner, desimal, oktal, atau heksadesimal
- **Hasil Ganda**: Menampilkan hasil dalam sistem asal dan desimal

### ⚠️ Tab Simulasi Kesalahan
- **Bit Flip**: Simulasi perubahan bit acak
- **Salah Konversi**: Simulasi kesalahan dalam proses konversi
- **Salah Interpretasi**: Simulasi salah mengidentifikasi sistem bilangan
- **Overflow/Underflow**: Simulasi nilai melebihi atau kurang dari batas
- **Analisis Dampak**: Menampilkan dampak kesalahan dalam desimal

### 🔍 Tab Deteksi Kesalahan
- **Validasi Konversi**: Memeriksa apakah hasil konversi benar
- **Analisis Kesalahan**: Mengidentifikasi jenis dan tingkat kesalahan
- **Tingkat Kepercayaan**: Menampilkan seberapa yakin deteksi kesalahan
- **Saran Perbaikan**: Memberikan informasi tentang kesalahan yang terdeteksi

### 📜 Tab Riwayat
- **Riwayat Lengkap**: Menampilkan semua konversi yang pernah dilakukan
- **Refresh Manual**: Memperbarui tampilan riwayat
- **Hapus Riwayat**: Membersihkan semua riwayat konversi
- **Tampilan Terbatas**: Menampilkan 20 konversi terakhir

### ❓ Tab Bantuan
- **Panduan Lengkap**: Penjelasan semua fitur aplikasi
- **Tips Penggunaan**: Saran untuk menggunakan aplikasi dengan optimal
- **Contoh Praktis**: Contoh-contoh penggunaan fitur
- **Troubleshooting**: Solusi untuk masalah umum

## 🎯 Sistem Bilangan yang Didukung

| Sistem | Base | Digit | Contoh |
|--------|------|-------|--------|
| **Biner** | 2 | 0, 1 | 101010 |
| **Desimal** | 10 | 0-9 | 42 |
| **Oktal** | 8 | 0-7 | 52 |
| **Heksadesimal** | 16 | 0-9, A-F | 2A |

## 💡 Cara Penggunaan

### Konversi Dasar
1. Pilih **Tab Konversi**
2. Pilih sistem asal dari dropdown
3. Masukkan nilai yang akan dikonversi
4. Pilih sistem tujuan
5. Klik tombol **"🔄 Konversi"**
6. Lihat hasil di area output

### Operasi Aritmatika
1. Pilih **Tab Aritmatika**
2. Pilih sistem bilangan
3. Masukkan nilai pertama dan kedua
4. Pilih operasi yang diinginkan
5. Klik tombol **"🧮 Hitung"**
6. Lihat hasil operasi

### Simulasi Kesalahan
1. Pilih **Tab Simulasi Kesalahan**
2. Pilih sistem bilangan
3. Masukkan nilai
4. Pilih jenis kesalahan
5. Klik tombol **"⚠️ Simulasikan Kesalahan"**
6. Analisis dampak kesalahan

### Deteksi Kesalahan
1. Pilih **Tab Deteksi Kesalahan**
2. Masukkan nilai asal dan hasil konversi
3. Pilih sistem asal dan tujuan
4. Klik tombol **"🔍 Deteksi Kesalahan"**
5. Lihat analisis kesalahan

## 🛠️ Persyaratan Sistem

- **Python**: 3.6 atau lebih baru
- **Tkinter**: Biasanya sudah terinstall dengan Python
- **Dependencies**: Tidak ada dependency eksternal

## 📁 Struktur File

```
├── gui_simulator.py          # GUI utama
├── demo_gui.py              # GUI dengan fitur demo
├── number_system_simulator.py # Engine konversi (CLI)
├── test_simulator.py        # Test suite
├── contoh_penggunaan.py     # Contoh penggunaan
├── demo.py                  # Demo CLI
└── README_GUI.md           # Dokumentasi GUI
```

## 🎨 Fitur GUI

### Interface Modern
- **Tab-based Layout**: Organisasi fitur dalam tab yang mudah diakses
- **Real-time Validation**: Validasi input secara real-time
- **Error Handling**: Penanganan error yang user-friendly
- **Responsive Design**: Interface yang responsif dan mudah digunakan

### User Experience
- **Tooltips**: Bantuan kontekstual untuk setiap fitur
- **Status Messages**: Pesan status yang informatif
- **Progress Indicators**: Indikator untuk operasi yang memakan waktu
- **Keyboard Shortcuts**: Shortcut keyboard untuk efisiensi

### Visual Elements
- **Icons**: Ikon yang jelas untuk setiap fitur
- **Color Coding**: Pengkodean warna untuk status dan jenis data
- **Typography**: Tipografi yang mudah dibaca
- **Layout**: Layout yang bersih dan terorganisir

## 🔧 Troubleshooting

### Masalah Umum

**Q: GUI tidak terbuka**
A: Pastikan tkinter terinstall: `python -m tkinter`

**Q: Error "Module not found"**
A: Pastikan semua file ada di direktori yang sama

**Q: Input tidak valid**
A: Periksa format input sesuai sistem bilangan yang dipilih

**Q: Hasil tidak muncul**
A: Pastikan input valid dan klik tombol yang sesuai

### Tips Penggunaan

1. **Gunakan Huruf Kapital**: Untuk heksadesimal, gunakan A-F (bukan a-f)
2. **Validasi Input**: Pastikan input sesuai dengan sistem bilangan
3. **Riwayat**: Gunakan tab riwayat untuk melihat konversi sebelumnya
4. **Bantuan**: Konsultasi tab bantuan untuk panduan lengkap

## 🎓 Contoh Penggunaan

### Konversi 42 (Desimal)
- **Biner**: 101010
- **Oktal**: 52
- **Heksadesimal**: 2A

### Operasi Biner: 1010 + 110
- **Hasil Biner**: 10000
- **Hasil Desimal**: 16

### Simulasi Bit Flip: 1010101
- **Hasil**: 1010001 (bit ke-3 di-flip)
- **Dampak**: Selisih 4 dalam desimal

## 🚀 Pengembangan

### Menambah Fitur Baru
1. Edit `gui_simulator.py`
2. Tambahkan tab baru di `create_widgets()`
3. Implementasikan handler di kelas utama
4. Test fitur baru

### Customization
- **Theme**: Ubah style di `setup_styles()`
- **Layout**: Modifikasi layout di `create_widgets()`
- **Validation**: Tambahkan validasi di handler methods

## 📞 Dukungan

Jika mengalami masalah atau memiliki saran:
1. Periksa tab **Bantuan** di aplikasi
2. Lihat contoh di `contoh_penggunaan.py`
3. Jalankan test suite untuk memastikan fungsi normal

---

**🎉 Selamat menggunakan GUI Simulator Sistem Bilangan!**

*Program ini dibuat untuk membantu pembelajaran dan pemahaman sistem bilangan dengan interface yang user-friendly dan fitur yang lengkap.*
