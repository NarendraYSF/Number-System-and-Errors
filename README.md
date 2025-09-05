# 🔢 Simulator Sistem Bilangan dengan Deteksi Kesalahan

Aplikasi lengkap untuk konversi antar sistem bilangan, operasi aritmatika, simulasi kesalahan, dan deteksi kesalahan dengan antarmuka GUI yang user-friendly.

## 🚀 Fitur Utama

### 🔄 Konversi Antar Sistem Bilangan
- **Biner (Base-2)**: Menggunakan digit 0, 1
- **Desimal (Base-10)**: Menggunakan digit 0-9
- **Oktal (Base-8)**: Menggunakan digit 0-7
- **Heksadesimal (Base-16)**: Menggunakan digit 0-9, A-F

### 🧮 Operasi Aritmatika
- Penjumlahan (+), Pengurangan (-), Perkalian (*)
- Pembagian (/), Modulo (%), Pangkat (**)
- Operasi dalam sistem bilangan apapun
- Hasil dalam sistem asal dan desimal

### ⚠️ Simulasi Kesalahan
- **Bit Flip**: Perubahan bit acak (0→1 atau 1→0)
- **Salah Konversi**: Kesalahan dalam proses konversi
- **Salah Interpretasi**: Salah mengidentifikasi sistem bilangan
- **Overflow/Underflow**: Nilai melebihi atau kurang dari batas

### 🔍 Deteksi Kesalahan
- Validasi hasil konversi
- Analisis jenis dan tingkat kesalahan
- Tingkat kepercayaan deteksi
- Saran perbaikan

### 📜 Riwayat dan Bantuan
- Riwayat konversi otomatis
- Bantuan lengkap dan panduan
- Interface yang intuitif

## 🖥️ Antarmuka

### GUI (Grafis)
- **Modern Interface**: Tab-based layout yang mudah digunakan
- **Real-time Validation**: Validasi input secara real-time
- **Error Handling**: Penanganan error yang user-friendly
- **Responsive Design**: Interface yang responsif

### CLI (Command Line)
- **Interactive Mode**: Mode interaktif dengan menu
- **Demo Mode**: Demonstrasi otomatis fitur-fitur
- **Batch Mode**: Mode batch untuk operasi massal

## 📁 Struktur Proyek

```
├── gui_simulator.py          # GUI utama dengan tkinter
├── demo_gui.py              # GUI dengan fitur demo
├── number_system_simulator.py # Engine konversi (CLI)
├── test_simulator.py        # Test suite untuk engine
├── test_gui.py              # Test suite untuk GUI
├── run_gui.py               # Script launcher GUI
├── run_all_tests.py         # Script untuk menjalankan semua test
├── config_gui.py            # Konfigurasi GUI
├── contoh_penggunaan.py     # Contoh penggunaan
├── demo.py                  # Demo CLI
├── run_gui.bat              # Batch file untuk Windows
├── run_gui.sh               # Shell script untuk Linux/Mac
├── requirements.txt         # Dependencies
├── README.md                # Dokumentasi utama
└── README_GUI.md            # Dokumentasi GUI
```

## 🚀 Cara Menjalankan

### 1. GUI (Antarmuka Grafis)

#### Windows
```bash
# GUI standar
python gui_simulator.py

# GUI dengan demo
python demo_gui.py

# Menggunakan batch file
run_gui.bat
```

#### Linux/Mac
```bash
# GUI standar
python3 gui_simulator.py

# GUI dengan demo
python3 demo_gui.py

# Menggunakan shell script
./run_gui.sh
```

#### Cross-platform
```bash
# Menggunakan script launcher
python run_gui.py          # GUI standar
python run_gui.py --demo   # GUI dengan demo
python run_gui.py --help   # Bantuan
```

### 2. CLI (Command Line Interface)

```bash
# Mode interaktif
python number_system_simulator.py

# Demo otomatis
python demo.py

# Contoh penggunaan
python contoh_penggunaan.py
```

### 3. Test Suite

```bash
# Test engine konversi
python test_simulator.py

# Test GUI
python test_gui.py

# Semua test
python run_all_tests.py
```

## 🛠️ Persyaratan Sistem

- **Python**: 3.6 atau lebih baru
- **Tkinter**: Biasanya sudah terinstall dengan Python
- **OS**: Windows, Linux, macOS
- **Memory**: Minimal 100MB RAM
- **Storage**: Minimal 10MB ruang disk

## 📋 Instalasi

### 1. Clone atau Download
```bash
git clone <repository-url>
cd simulator-sistem-bilangan
```

### 2. Periksa Dependencies
```bash
python run_all_tests.py
```

### 3. Jalankan Aplikasi
```bash
# GUI
python gui_simulator.py

# CLI
python number_system_simulator.py
```

## 💡 Cara Penggunaan

### GUI Mode

1. **Konversi Dasar**
   - Pilih tab "Konversi"
   - Pilih sistem asal dan tujuan
   - Masukkan nilai
   - Klik "Konversi"

2. **Operasi Aritmatika**
   - Pilih tab "Aritmatika"
   - Pilih sistem bilangan
   - Masukkan dua nilai dan operasi
   - Klik "Hitung"

3. **Simulasi Kesalahan**
   - Pilih tab "Simulasi Kesalahan"
   - Pilih sistem dan jenis kesalahan
   - Masukkan nilai
   - Klik "Simulasikan Kesalahan"

4. **Deteksi Kesalahan**
   - Pilih tab "Deteksi Kesalahan"
   - Masukkan nilai asal dan hasil
   - Pilih sistem asal dan tujuan
   - Klik "Deteksi Kesalahan"

### CLI Mode

1. **Mode Interaktif**
   ```bash
   python number_system_simulator.py
   # Pilih mode: 1. Interaktif, 2. Demo
   ```

2. **Demo Otomatis**
   ```bash
   python demo.py
   ```

## 🎯 Contoh Penggunaan

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

### Deteksi Kesalahan
- **Input**: 42 (desimal) → 101010 (biner) ✅ BENAR
- **Input**: 42 (desimal) → 101011 (biner) ❌ SALAH

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

## 🧪 Testing

### Menjalankan Test
```bash
# Test engine konversi
python test_simulator.py

# Test GUI
python test_gui.py

# Semua test
python run_all_tests.py
```

### Coverage Test
```bash
# Install coverage (opsional)
pip install coverage

# Jalankan test dengan coverage
coverage run -m pytest test_simulator.py
coverage report
```

## 🚀 Pengembangan

### Menambah Fitur Baru
1. Edit file yang sesuai
2. Tambahkan test untuk fitur baru
3. Update dokumentasi
4. Jalankan test suite

### Customization
- **Theme**: Ubah `config_gui.py`
- **Layout**: Modifikasi `gui_simulator.py`
- **Validation**: Tambahkan validasi di handler methods

## 📊 Performa

### Benchmark
- **Startup Time**: < 5 detik
- **Memory Usage**: < 100MB
- **Conversion Speed**: < 1ms per konversi
- **GUI Responsiveness**: Real-time

### Optimization
- Caching untuk konversi yang sering digunakan
- Lazy loading untuk komponen GUI
- Background processing untuk operasi berat

## 🤝 Kontribusi

### Cara Berkontribusi
1. Fork repository
2. Buat branch fitur baru
3. Commit perubahan
4. Push ke branch
5. Buat Pull Request

### Guidelines
- Ikuti PEP 8 untuk Python
- Tambahkan test untuk fitur baru
- Update dokumentasi
- Test di berbagai platform

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file LICENSE untuk detail.

## 📞 Dukungan

### Bantuan
- Lihat tab **Bantuan** di aplikasi
- Periksa `README_GUI.md` untuk panduan GUI
- Jalankan test suite untuk memastikan fungsi normal

### Bug Report
- Gunakan GitHub Issues
- Sertakan informasi sistem
- Sertakan langkah reproduksi

## 🎓 Tentang

### Tujuan
Program ini dibuat untuk membantu pembelajaran dan pemahaman sistem bilangan dengan interface yang user-friendly dan fitur yang lengkap.

### Fitur Khusus
- **Educational**: Fokus pada pembelajaran
- **User-friendly**: Interface yang mudah digunakan
- **Comprehensive**: Fitur lengkap untuk semua kebutuhan
- **Robust**: Penanganan error yang baik

### Teknologi
- **Python 3.6+**: Bahasa pemrograman utama
- **Tkinter**: Framework GUI
- **Unittest**: Framework testing
- **Type Hints**: Untuk kode yang lebih jelas

---

**🎉 Selamat menggunakan Simulator Sistem Bilangan!**

*Program ini dibuat untuk membantu pembelajaran dan pemahaman sistem bilangan dengan interface yang user-friendly dan fitur yang lengkap.*