# 🔢 Simulator Sistem Bilangan dengan Deteksi Kesalahan

Program Python komprehensif yang mensimulasikan berbagai sistem bilangan (biner, desimal, heksadesimal, oktal) dan mendemonstrasikan konversi antar sistem dengan kemampuan mendeteksi dan mensimulasikan kesalahan umum.

## ✨ Fitur Utama

### 🔄 Konversi Sistem Bilangan
- **Biner (Base-2)**: Menggunakan digit 0, 1
- **Desimal (Base-10)**: Menggunakan digit 0-9  
- **Oktal (Base-8)**: Menggunakan digit 0-7
- **Heksadesimal (Base-16)**: Menggunakan digit 0-9, A-F

### ⚠️ Simulasi Kesalahan
- **Bit Flip**: Perubahan bit acak (0→1 atau 1→0)
- **Salah Konversi**: Kesalahan dalam proses konversi
- **Salah Interpretasi**: Salah mengidentifikasi sistem bilangan
- **Overflow**: Nilai melebihi kapasitas
- **Underflow**: Nilai kurang dari minimum

### 🔍 Deteksi Kesalahan
- Analisis otomatis hasil konversi
- Tingkat kepercayaan deteksi
- Identifikasi jenis kesalahan

### 🧮 Operasi Aritmatika
- Penjumlahan, pengurangan, perkalian, pembagian
- Modulo dan operasi pangkat
- Hasil dalam sistem bilangan yang dipilih

## 🚀 Cara Menjalankan

### Menjalankan Program Utama
```bash
python number_system_simulator.py
```

### Menjalankan Test Suite
```bash
python test_simulator.py
```

## 📋 Menu Program

### 1. 🔄 Konversi Antar Sistem Bilangan
Konversi nilai dari satu sistem bilangan ke sistem lainnya dengan akurasi tinggi.

**Contoh:**
- Desimal 42 → Biner: 101010
- Heksadesimal 2A → Oktal: 52

### 2. 📊 Tabel Konversi Lengkap
Menampilkan konversi satu nilai ke semua sistem bilangan sekaligus.

### 3. 🧮 Operasi Aritmatika
Melakukan operasi matematika dalam sistem bilangan tertentu.

**Operasi yang didukung:**
- ➕ Penjumlahan (+)
- ➖ Pengurangan (-)
- ✖️ Perkalian (*)
- ➗ Pembagian (/)
- 📐 Modulo (%)
- 🔺 Pangkat (**)

### 4. ⚠️ Simulasi Kesalahan
Mensimulasikan berbagai jenis kesalahan yang umum terjadi dalam konversi sistem bilangan.

### 5. 🔍 Deteksi Kesalahan Konversi
Menganalisis hasil konversi untuk mendeteksi kemungkinan kesalahan.

### 6. 📜 Riwayat Konversi
Menampilkan riwayat konversi yang telah dilakukan.

### 7. ❓ Bantuan dan Informasi
Panduan lengkap penggunaan program.

## 🔧 Struktur Kode

### Kelas Utama

#### `KonverterSistemBilangan`
Kelas inti yang menangani:
- Konversi antar sistem bilangan
- Validasi input
- Simulasi dan deteksi kesalahan
- Operasi aritmatika

#### `InterfacePengguna`
Kelas untuk interaksi pengguna:
- Menu interaktif
- Input validation
- Tampilan hasil yang user-friendly

#### Enumerasi
- `SistemBilangan`: Mendefinisikan sistem bilangan yang didukung
- `JenisKesalahan`: Mendefinisikan jenis kesalahan yang dapat disimulasikan

## 📝 Contoh Penggunaan

### Konversi Sederhana
```python
from number_system_simulator import KonverterSistemBilangan, SistemBilangan

konverter = KonverterSistemBilangan()

# Konversi desimal 42 ke biner
hasil = konverter.konversi("42", SistemBilangan.DESIMAL, SistemBilangan.BINER)
print(f"42 desimal = {hasil} biner")  # Output: 42 desimal = 101010 biner
```

### Simulasi Kesalahan
```python
from number_system_simulator import JenisKesalahan

# Simulasi bit flip pada nilai biner
hasil_error, penjelasan = konverter.simulasi_kesalahan(
    "1010101", 
    SistemBilangan.BINER, 
    JenisKesalahan.BIT_FLIP
)
print(f"Hasil dengan kesalahan: {hasil_error}")
print(f"Penjelasan: {penjelasan}")
```

### Deteksi Kesalahan
```python
# Deteksi kesalahan dalam hasil konversi
analisis = konverter.deteksi_kesalahan_konversi(
    "42",           # nilai asal
    "101011",       # hasil konversi (salah)
    SistemBilangan.DESIMAL,
    SistemBilangan.BINER
)

if analisis['ada_kesalahan']:
    print("❌ Kesalahan terdeteksi!")
    print(f"Hasil yang benar: {analisis['hasil_benar']}")
```

## 🛡️ Validasi dan Error Handling

Program ini dilengkapi dengan:

### Validasi Input
- Pemeriksaan format input sesuai sistem bilangan
- Regex validation untuk setiap sistem
- Penanganan input kosong atau invalid

### Error Handling
- Try-catch untuk semua operasi kritis
- Pesan error yang informatif dalam bahasa Indonesia
- Graceful handling untuk interrupt (Ctrl+C)

### Batasan
- Hanya mendukung bilangan positif
- Eksponen dibatasi maksimal 20 untuk mencegah overflow
- Input maksimal terbatas oleh kapasitas integer Python

## 🎯 Tujuan Edukatif

Program ini dirancang untuk:

1. **Memahami Sistem Bilangan**: Memberikan pemahaman praktis tentang berbagai sistem bilangan
2. **Belajar Konversi**: Mendemonstrasikan cara konversi yang benar antar sistem
3. **Mengenali Kesalahan**: Mengajarkan jenis-jenis kesalahan yang umum terjadi
4. **Validasi**: Menunjukkan pentingnya validasi input dalam pemrograman

## 🌟 Keunggulan

- **Modular**: Kode terstruktur dengan kelas dan fungsi yang terpisah
- **Dokumentasi Lengkap**: Setiap fungsi memiliki docstring dalam bahasa Indonesia
- **User-Friendly**: Interface yang intuitif dengan emoji dan pesan yang jelas
- **Robust**: Validasi input yang ketat dan error handling yang baik
- **Educational**: Dirancang untuk tujuan pembelajaran dengan contoh yang jelas

## 🔮 Pengembangan Lanjutan

Fitur yang dapat ditambahkan:
- Support untuk bilangan negatif dan pecahan
- Sistem bilangan custom (base-n)
- Export hasil ke file
- Visualisasi grafis konversi
- Mode batch processing
- API untuk integrasi dengan aplikasi lain

## 📞 Dukungan

Program ini dibuat dengan Python 3.6+ dan tidak memerlukan library eksternal. Semua fitur menggunakan standard library Python.

---

**Selamat belajar sistem bilangan! 🎓**
