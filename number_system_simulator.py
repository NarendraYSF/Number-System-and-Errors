#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulator Sistem Bilangan dengan Deteksi Kesalahan
==================================================

Program ini mensimulasikan berbagai sistem bilangan (biner, desimal, heksadesimal, oktal)
dan mendemonstrasikan konversi antar sistem dengan kemampuan mendeteksi dan mensimulasikan
kesalahan umum yang terjadi selama konversi atau operasi.

Fitur:
- Konversi antar sistem bilangan
- Simulasi kesalahan umum (bit flip, salah konversi, salah interpretasi)
- Validasi input yang kuat
- Interface pengguna interaktif dalam bahasa Indonesia
- Implementasi modular dengan komentar lengkap

Penulis: AI Assistant
Tanggal: 2024
"""

import random
import re
from typing import Dict, List, Tuple, Optional, Union
from enum import Enum


class SistemBilangan(Enum):
    """Enumerasi untuk berbagai sistem bilangan yang didukung"""
    BINER = "biner"
    DESIMAL = "desimal"
    HEKSADESIMAL = "heksadesimal"
    OKTAL = "oktal"


class JenisKesalahan(Enum):
    """Enumerasi untuk berbagai jenis kesalahan yang dapat disimulasikan"""
    BIT_FLIP = "bit_flip"
    SALAH_KONVERSI = "salah_konversi"
    SALAH_INTERPRETASI = "salah_interpretasi"
    OVERFLOW = "overflow"
    UNDERFLOW = "underflow"


class KonverterSistemBilangan:
    """
    Kelas utama untuk konversi antar sistem bilangan dengan kemampuan simulasi kesalahan
    
    Kelas ini menyediakan metode untuk:
    - Konversi antar berbagai sistem bilangan
    - Simulasi kesalahan umum
    - Validasi input
    - Deteksi kesalahan
    """
    
    def __init__(self):
        """Inisialisasi konverter dengan konfigurasi default"""
        self.riwayat_konversi: List[Dict] = []
        self.probabilitas_kesalahan = 0.1  # 10% kemungkinan kesalahan saat simulasi
        
    def validasi_input(self, nilai: str, sistem: SistemBilangan) -> bool:
        """
        Memvalidasi apakah input sesuai dengan sistem bilangan yang dipilih
        
        Args:
            nilai (str): Nilai yang akan divalidasi
            sistem (SistemBilangan): Sistem bilangan yang digunakan
            
        Returns:
            bool: True jika valid, False jika tidak valid
        """
        try:
            nilai = nilai.strip().upper()
            
            if sistem == SistemBilangan.BINER:
                return bool(re.match(r'^[01]+$', nilai))
            elif sistem == SistemBilangan.DESIMAL:
                return bool(re.match(r'^[0-9]+$', nilai))
            elif sistem == SistemBilangan.OKTAL:
                return bool(re.match(r'^[0-7]+$', nilai))
            elif sistem == SistemBilangan.HEKSADESIMAL:
                return bool(re.match(r'^[0-9A-F]+$', nilai))
            
            return False
        except Exception:
            return False
    
    def ke_desimal(self, nilai: str, sistem_asal: SistemBilangan) -> int:
        """
        Mengkonversi nilai dari sistem bilangan tertentu ke desimal
        
        Args:
            nilai (str): Nilai yang akan dikonversi
            sistem_asal (SistemBilangan): Sistem bilangan asal
            
        Returns:
            int: Nilai dalam sistem desimal
            
        Raises:
            ValueError: Jika input tidak valid
        """
        if not self.validasi_input(nilai, sistem_asal):
            raise ValueError(f"Input '{nilai}' tidak valid untuk sistem {sistem_asal.value}")
        
        nilai = nilai.strip().upper()
        
        if sistem_asal == SistemBilangan.BINER:
            return int(nilai, 2)
        elif sistem_asal == SistemBilangan.DESIMAL:
            return int(nilai, 10)
        elif sistem_asal == SistemBilangan.OKTAL:
            return int(nilai, 8)
        elif sistem_asal == SistemBilangan.HEKSADESIMAL:
            return int(nilai, 16)
        
        raise ValueError(f"Sistem bilangan {sistem_asal} tidak didukung")
    
    def dari_desimal(self, nilai_desimal: int, sistem_tujuan: SistemBilangan) -> str:
        """
        Mengkonversi nilai desimal ke sistem bilangan tertentu
        
        Args:
            nilai_desimal (int): Nilai dalam sistem desimal
            sistem_tujuan (SistemBilangan): Sistem bilangan tujuan
            
        Returns:
            str: Nilai dalam sistem bilangan tujuan
        """
        if nilai_desimal < 0:
            raise ValueError("Program ini hanya mendukung bilangan positif")
        
        if sistem_tujuan == SistemBilangan.BINER:
            return bin(nilai_desimal)[2:]  # Menghilangkan prefix '0b'
        elif sistem_tujuan == SistemBilangan.DESIMAL:
            return str(nilai_desimal)
        elif sistem_tujuan == SistemBilangan.OKTAL:
            return oct(nilai_desimal)[2:]  # Menghilangkan prefix '0o'
        elif sistem_tujuan == SistemBilangan.HEKSADESIMAL:
            return hex(nilai_desimal)[2:].upper()  # Menghilangkan prefix '0x' dan uppercase
        
        raise ValueError(f"Sistem bilangan {sistem_tujuan} tidak didukung")
    
    def konversi(self, nilai: str, sistem_asal: SistemBilangan, 
                sistem_tujuan: SistemBilangan) -> str:
        """
        Melakukan konversi langsung antar sistem bilangan
        
        Args:
            nilai (str): Nilai yang akan dikonversi
            sistem_asal (SistemBilangan): Sistem bilangan asal
            sistem_tujuan (SistemBilangan): Sistem bilangan tujuan
            
        Returns:
            str: Hasil konversi
        """
        # Konversi ke desimal terlebih dahulu, kemudian ke sistem tujuan
        nilai_desimal = self.ke_desimal(nilai, sistem_asal)
        hasil = self.dari_desimal(nilai_desimal, sistem_tujuan)
        
        # Simpan riwayat konversi
        self.riwayat_konversi.append({
            'nilai_asal': nilai,
            'sistem_asal': sistem_asal.value,
            'sistem_tujuan': sistem_tujuan.value,
            'hasil': hasil,
            'nilai_desimal': nilai_desimal
        })
        
        return hasil
    
    def simulasi_bit_flip(self, nilai_biner: str) -> str:
        """
        Mensimulasikan kesalahan bit flip pada nilai biner
        
        Args:
            nilai_biner (str): Nilai biner yang akan dimodifikasi
            
        Returns:
            str: Nilai biner dengan bit yang di-flip
        """
        if not nilai_biner:
            return nilai_biner
            
        # Pilih posisi bit secara acak untuk di-flip
        posisi = random.randint(0, len(nilai_biner) - 1)
        bit_list = list(nilai_biner)
        
        # Flip bit (0 menjadi 1, 1 menjadi 0)
        bit_list[posisi] = '1' if bit_list[posisi] == '0' else '0'
        
        return ''.join(bit_list)
    
    def simulasi_salah_konversi(self, nilai: str, sistem_asal: SistemBilangan) -> str:
        """
        Mensimulasikan kesalahan konversi yang umum terjadi
        
        Args:
            nilai (str): Nilai asal
            sistem_asal (SistemBilangan): Sistem bilangan asal
            
        Returns:
            str: Hasil konversi yang salah
        """
        # Berbagai jenis kesalahan konversi yang umum
        kesalahan_umum = [
            lambda x: x[::-1],  # Membalik urutan digit
            lambda x: x[1:] if len(x) > 1 else '0',  # Menghilangkan digit pertama
            lambda x: x + '0',  # Menambah digit 0 di akhir
            lambda x: '0' + x,  # Menambah digit 0 di awal
        ]
        
        if sistem_asal == SistemBilangan.HEKSADESIMAL:
            # Kesalahan khusus untuk heksadesimal
            kesalahan_hex = [
                lambda x: x.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15'),
                lambda x: x.lower(),  # Menggunakan huruf kecil
            ]
            kesalahan_umum.extend(kesalahan_hex)
        
        # Pilih jenis kesalahan secara acak
        kesalahan_terpilih = random.choice(kesalahan_umum)
        return kesalahan_terpilih(nilai)
    
    def simulasi_salah_interpretasi(self, nilai: str) -> Tuple[str, str]:
        """
        Mensimulasikan kesalahan interpretasi sistem bilangan
        
        Args:
            nilai (str): Nilai yang akan disalahinterpretasikan
            
        Returns:
            Tuple[str, str]: (sistem_yang_diasumsikan, penjelasan_kesalahan)
        """
        # Simulasi salah interpretasi sistem bilangan
        interpretasi_salah = [
            ("Menginterpretasikan biner sebagai desimal", "decimal"),
            ("Menginterpretasikan oktal sebagai desimal", "decimal"),
            ("Menginterpretasikan heksadesimal tanpa prefix sebagai desimal", "decimal"),
            ("Mengabaikan digit yang tidak valid", "truncated"),
        ]
        
        kesalahan_terpilih = random.choice(interpretasi_salah)
        return kesalahan_terpilih[1], kesalahan_terpilih[0]
    
    def deteksi_kesalahan_konversi(self, nilai_asal: str, hasil_konversi: str, 
                                  sistem_asal: SistemBilangan, 
                                  sistem_tujuan: SistemBilangan) -> Dict:
        """
        Mendeteksi kemungkinan kesalahan dalam hasil konversi
        
        Args:
            nilai_asal (str): Nilai asal
            hasil_konversi (str): Hasil konversi yang akan diperiksa
            sistem_asal (SistemBilangan): Sistem bilangan asal
            sistem_tujuan (SistemBilangan): Sistem bilangan tujuan
            
        Returns:
            Dict: Informasi tentang kesalahan yang terdeteksi
        """
        try:
            # Lakukan konversi yang benar untuk perbandingan
            hasil_benar = self.konversi(nilai_asal, sistem_asal, sistem_tujuan)
            
            kesalahan_terdeteksi = {
                'ada_kesalahan': hasil_konversi != hasil_benar,
                'hasil_benar': hasil_benar,
                'hasil_input': hasil_konversi,
                'jenis_kesalahan': [],
                'tingkat_kepercayaan': 0.0
            }
            
            if kesalahan_terdeteksi['ada_kesalahan']:
                # Analisis jenis kesalahan
                if len(hasil_konversi) != len(hasil_benar):
                    kesalahan_terdeteksi['jenis_kesalahan'].append("Panjang hasil tidak sesuai")
                
                # Hitung perbedaan karakter
                perbedaan = sum(1 for a, b in zip(hasil_konversi, hasil_benar) if a != b)
                if perbedaan == 1:
                    kesalahan_terdeteksi['jenis_kesalahan'].append("Kemungkinan kesalahan satu digit")
                elif perbedaan > len(hasil_benar) * 0.5:
                    kesalahan_terdeteksi['jenis_kesalahan'].append("Kesalahan sistematis atau salah interpretasi")
                
                # Hitung tingkat kepercayaan deteksi
                kesalahan_terdeteksi['tingkat_kepercayaan'] = min(1.0, perbedaan / len(hasil_benar))
            
            return kesalahan_terdeteksi
            
        except Exception as e:
            return {
                'ada_kesalahan': True,
                'hasil_benar': 'Tidak dapat dihitung',
                'hasil_input': hasil_konversi,
                'jenis_kesalahan': [f"Kesalahan validasi: {str(e)}"],
                'tingkat_kepercayaan': 1.0
            }
    
    def simulasi_kesalahan(self, nilai: str, sistem: SistemBilangan, 
                          jenis_kesalahan: JenisKesalahan) -> Tuple[str, str]:
        """
        Mensimulasikan berbagai jenis kesalahan
        
        Args:
            nilai (str): Nilai asal
            sistem (SistemBilangan): Sistem bilangan
            jenis_kesalahan (JenisKesalahan): Jenis kesalahan yang akan disimulasikan
            
        Returns:
            Tuple[str, str]: (hasil_dengan_kesalahan, penjelasan_kesalahan)
        """
        if jenis_kesalahan == JenisKesalahan.BIT_FLIP:
            if sistem == SistemBilangan.BINER:
                hasil_error = self.simulasi_bit_flip(nilai)
                return hasil_error, f"Bit flip pada posisi acak: {nilai} → {hasil_error}"
            else:
                # Konversi ke biner, lakukan bit flip, lalu konversi kembali
                nilai_biner = self.konversi(nilai, sistem, SistemBilangan.BINER)
                biner_error = self.simulasi_bit_flip(nilai_biner)
                hasil_error = self.konversi(biner_error, SistemBilangan.BINER, sistem)
                return hasil_error, f"Bit flip pada representasi biner: {nilai} → {hasil_error}"
        
        elif jenis_kesalahan == JenisKesalahan.SALAH_KONVERSI:
            hasil_error = self.simulasi_salah_konversi(nilai, sistem)
            return hasil_error, f"Kesalahan konversi: {nilai} → {hasil_error}"
        
        elif jenis_kesalahan == JenisKesalahan.SALAH_INTERPRETASI:
            sistem_salah, penjelasan = self.simulasi_salah_interpretasi(nilai)
            return nilai, f"Salah interpretasi: {penjelasan}"
        
        elif jenis_kesalahan == JenisKesalahan.OVERFLOW:
            # Simulasi overflow dengan menambah digit
            hasil_error = nilai + str(random.randint(1, 9))
            return hasil_error, f"Simulasi overflow: {nilai} → {hasil_error}"
        
        elif jenis_kesalahan == JenisKesalahan.UNDERFLOW:
            # Simulasi underflow dengan mengurangi digit
            if len(nilai) > 1:
                hasil_error = nilai[:-1]
                return hasil_error, f"Simulasi underflow: {nilai} → {hasil_error}"
            else:
                return "0", f"Simulasi underflow: {nilai} → 0"
        
        return nilai, "Tidak ada kesalahan yang disimulasikan"
    
    def tampilkan_tabel_konversi(self, nilai: str, sistem_asal: SistemBilangan) -> Dict[str, str]:
        """
        Membuat tabel konversi lengkap untuk satu nilai ke semua sistem bilangan
        
        Args:
            nilai (str): Nilai yang akan dikonversi
            sistem_asal (SistemBilangan): Sistem bilangan asal
            
        Returns:
            Dict[str, str]: Dictionary dengan hasil konversi ke semua sistem
        """
        hasil_konversi = {}
        
        try:
            for sistem_tujuan in SistemBilangan:
                if sistem_tujuan == sistem_asal:
                    hasil_konversi[sistem_tujuan.value] = nilai
                else:
                    hasil_konversi[sistem_tujuan.value] = self.konversi(nilai, sistem_asal, sistem_tujuan)
        
        except Exception as e:
            hasil_konversi['error'] = str(e)
        
        return hasil_konversi
    
    def operasi_aritmatika(self, nilai1: str, nilai2: str, operasi: str, 
                          sistem: SistemBilangan) -> Dict:
        """
        Melakukan operasi aritmatika pada dua nilai dalam sistem bilangan tertentu
        
        Args:
            nilai1 (str): Nilai pertama
            nilai2 (str): Nilai kedua
            operasi (str): Jenis operasi (+, -, *, /, %, **)
            sistem (SistemBilangan): Sistem bilangan yang digunakan
            
        Returns:
            Dict: Hasil operasi dan informasi tambahan
        """
        try:
            # Konversi ke desimal untuk perhitungan
            des1 = self.ke_desimal(nilai1, sistem)
            des2 = self.ke_desimal(nilai2, sistem)
            
            # Lakukan operasi
            if operasi == '+':
                hasil_desimal = des1 + des2
            elif operasi == '-':
                hasil_desimal = des1 - des2
            elif operasi == '*':
                hasil_desimal = des1 * des2
            elif operasi == '/':
                if des2 == 0:
                    raise ValueError("Pembagian dengan nol tidak diperbolehkan")
                hasil_desimal = des1 // des2  # Pembagian integer
            elif operasi == '%':
                if des2 == 0:
                    raise ValueError("Modulo dengan nol tidak diperbolehkan")
                hasil_desimal = des1 % des2
            elif operasi == '**':
                if des2 > 20:  # Batasi eksponen untuk mencegah hasil yang terlalu besar
                    raise ValueError("Eksponen terlalu besar (maksimal 20)")
                hasil_desimal = des1 ** des2
            else:
                raise ValueError(f"Operasi '{operasi}' tidak didukung")
            
            if hasil_desimal < 0:
                raise ValueError("Hasil negatif tidak didukung dalam program ini")
            
            # Konversi hasil kembali ke sistem asal
            hasil_sistem = self.dari_desimal(hasil_desimal, sistem)
            
            return {
                'berhasil': True,
                'hasil_desimal': hasil_desimal,
                'hasil_sistem': hasil_sistem,
                'operasi': f"{nilai1} {operasi} {nilai2}",
                'sistem': sistem.value
            }
            
        except Exception as e:
            return {
                'berhasil': False,
                'error': str(e),
                'operasi': f"{nilai1} {operasi} {nilai2}",
                'sistem': sistem.value
            }


class InterfacePengguna:
    """
    Kelas untuk menangani interaksi dengan pengguna
    
    Menyediakan menu interaktif dan antarmuka yang user-friendly
    """
    
    def __init__(self):
        """Inisialisasi interface dengan konverter"""
        self.konverter = KonverterSistemBilangan()
        self.sistem_map = {
            '1': SistemBilangan.BINER,
            '2': SistemBilangan.DESIMAL,
            '3': SistemBilangan.OKTAL,
            '4': SistemBilangan.HEKSADESIMAL
        }
        
    def tampilkan_header(self):
        """Menampilkan header program"""
        print("=" * 70)
        print("🔢 SIMULATOR SISTEM BILANGAN DENGAN DETEKSI KESALAHAN 🔢")
        print("=" * 70)
        print("Program ini mensimulasikan konversi antar sistem bilangan dan")
        print("mendemonstrasikan berbagai jenis kesalahan yang mungkin terjadi.")
        print("=" * 70)
    
    def tampilkan_menu_utama(self):
        """Menampilkan menu utama"""
        print("\n📋 MENU UTAMA:")
        print("1. 🔄 Konversi Antar Sistem Bilangan")
        print("2. 📊 Tabel Konversi Lengkap")
        print("3. 🧮 Operasi Aritmatika")
        print("4. ⚠️  Simulasi Kesalahan")
        print("5. 🔍 Deteksi Kesalahan Konversi")
        print("6. 📜 Lihat Riwayat Konversi")
        print("7. ❓ Bantuan dan Informasi")
        print("8. 🚪 Keluar")
        print("-" * 50)
    
    def tampilkan_menu_sistem(self, judul: str = "Pilih Sistem Bilangan"):
        """Menampilkan menu pemilihan sistem bilangan"""
        print(f"\n{judul}:")
        print("1. 🔢 Biner (Binary)")
        print("2. 🔟 Desimal (Decimal)")
        print("3. 8️⃣  Oktal (Octal)")
        print("4. 🔠 Heksadesimal (Hexadecimal)")
    
    def pilih_sistem(self, prompt: str = "Masukkan pilihan sistem") -> Optional[SistemBilangan]:
        """
        Meminta pengguna memilih sistem bilangan
        
        Args:
            prompt (str): Pesan prompt untuk pengguna
            
        Returns:
            Optional[SistemBilangan]: Sistem bilangan yang dipilih atau None jika batal
        """
        while True:
            try:
                pilihan = input(f"{prompt} (1-4, atau 0 untuk kembali): ").strip()
                
                if pilihan == '0':
                    return None
                
                if pilihan in self.sistem_map:
                    return self.sistem_map[pilihan]
                else:
                    print("❌ Pilihan tidak valid. Silakan pilih 1-4.")
                    
            except KeyboardInterrupt:
                print("\n\n🚪 Program dihentikan oleh pengguna.")
                return None
    
    def input_nilai(self, sistem: SistemBilangan) -> Optional[str]:
        """
        Meminta input nilai dari pengguna dengan validasi
        
        Args:
            sistem (SistemBilangan): Sistem bilangan yang digunakan
            
        Returns:
            Optional[str]: Nilai yang diinput atau None jika batal
        """
        contoh = {
            SistemBilangan.BINER: "101010",
            SistemBilangan.DESIMAL: "42",
            SistemBilangan.OKTAL: "52",
            SistemBilangan.HEKSADESIMAL: "2A"
        }
        
        while True:
            try:
                nilai = input(f"Masukkan nilai {sistem.value} (contoh: {contoh[sistem]}, atau 0 untuk kembali): ").strip()
                
                if nilai == '0' and sistem != SistemBilangan.DESIMAL:
                    return None
                
                if self.konverter.validasi_input(nilai, sistem):
                    return nilai.upper() if sistem == SistemBilangan.HEKSADESIMAL else nilai
                else:
                    print(f"❌ Input tidak valid untuk sistem {sistem.value}.")
                    self.tampilkan_aturan_sistem(sistem)
                    
            except KeyboardInterrupt:
                print("\n\n🚪 Kembali ke menu utama.")
                return None
    
    def tampilkan_aturan_sistem(self, sistem: SistemBilangan):
        """Menampilkan aturan untuk sistem bilangan tertentu"""
        aturan = {
            SistemBilangan.BINER: "Hanya boleh menggunakan digit 0 dan 1",
            SistemBilangan.DESIMAL: "Hanya boleh menggunakan digit 0-9",
            SistemBilangan.OKTAL: "Hanya boleh menggunakan digit 0-7",
            SistemBilangan.HEKSADESIMAL: "Boleh menggunakan digit 0-9 dan huruf A-F"
        }
        print(f"ℹ️  Aturan {sistem.value}: {aturan[sistem]}")
    
    def konversi_interaktif(self):
        """Menu konversi interaktif"""
        print("\n🔄 KONVERSI ANTAR SISTEM BILANGAN")
        print("=" * 40)
        
        # Pilih sistem asal
        self.tampilkan_menu_sistem("Pilih sistem bilangan ASAL")
        sistem_asal = self.pilih_sistem("Pilih sistem asal")
        if not sistem_asal:
            return
        
        # Input nilai
        nilai = self.input_nilai(sistem_asal)
        if not nilai:
            return
        
        # Pilih sistem tujuan
        self.tampilkan_menu_sistem("Pilih sistem bilangan TUJUAN")
        sistem_tujuan = self.pilih_sistem("Pilih sistem tujuan")
        if not sistem_tujuan:
            return
        
        try:
            hasil = self.konverter.konversi(nilai, sistem_asal, sistem_tujuan)
            
            print(f"\n✅ HASIL KONVERSI:")
            print(f"   {sistem_asal.value.capitalize()}: {nilai}")
            print(f"   {sistem_tujuan.value.capitalize()}: {hasil}")
            
            # Tampilkan nilai desimal sebagai referensi
            nilai_desimal = self.konverter.ke_desimal(nilai, sistem_asal)
            print(f"   Nilai desimal: {nilai_desimal}")
            
        except Exception as e:
            print(f"❌ Kesalahan: {e}")
    
    def tabel_konversi_lengkap(self):
        """Menampilkan tabel konversi lengkap"""
        print("\n📊 TABEL KONVERSI LENGKAP")
        print("=" * 50)
        
        # Pilih sistem asal
        self.tampilkan_menu_sistem("Pilih sistem bilangan ASAL")
        sistem_asal = self.pilih_sistem("Pilih sistem asal")
        if not sistem_asal:
            return
        
        # Input nilai
        nilai = self.input_nilai(sistem_asal)
        if not nilai:
            return
        
        try:
            hasil_konversi = self.konverter.tampilkan_tabel_konversi(nilai, sistem_asal)
            
            print(f"\n📋 Tabel konversi untuk nilai '{nilai}' ({sistem_asal.value}):")
            print("-" * 50)
            
            for sistem, hasil in hasil_konversi.items():
                if sistem != 'error':
                    print(f"   {sistem.capitalize():<12}: {hasil}")
            
            if 'error' in hasil_konversi:
                print(f"❌ Kesalahan: {hasil_konversi['error']}")
                
        except Exception as e:
            print(f"❌ Kesalahan: {e}")
    
    def operasi_aritmatika_interaktif(self):
        """Menu operasi aritmatika interaktif"""
        print("\n🧮 OPERASI ARITMATIKA")
        print("=" * 30)
        
        # Pilih sistem bilangan
        self.tampilkan_menu_sistem("Pilih sistem bilangan untuk operasi")
        sistem = self.pilih_sistem("Pilih sistem")
        if not sistem:
            return
        
        # Input nilai pertama
        print(f"\nMasukkan nilai pertama dalam sistem {sistem.value}:")
        nilai1 = self.input_nilai(sistem)
        if not nilai1:
            return
        
        # Input nilai kedua
        print(f"Masukkan nilai kedua dalam sistem {sistem.value}:")
        nilai2 = self.input_nilai(sistem)
        if not nilai2:
            return
        
        # Pilih operasi
        print("\nPilih operasi:")
        print("1. ➕ Penjumlahan (+)")
        print("2. ➖ Pengurangan (-)")
        print("3. ✖️  Perkalian (*)")
        print("4. ➗ Pembagian (/)")
        print("5. 📐 Modulo (%)")
        print("6. 🔺 Pangkat (**)")
        
        operasi_map = {'1': '+', '2': '-', '3': '*', '4': '/', '5': '%', '6': '**'}
        
        while True:
            pilihan_op = input("Pilih operasi (1-6): ").strip()
            if pilihan_op in operasi_map:
                operasi = operasi_map[pilihan_op]
                break
            print("❌ Pilihan operasi tidak valid.")
        
        # Lakukan operasi
        hasil = self.konverter.operasi_aritmatika(nilai1, nilai2, operasi, sistem)
        
        print(f"\n📊 HASIL OPERASI:")
        if hasil['berhasil']:
            print(f"   Operasi: {hasil['operasi']}")
            print(f"   Sistem: {hasil['sistem']}")
            print(f"   Hasil ({sistem.value}): {hasil['hasil_sistem']}")
            print(f"   Hasil (desimal): {hasil['hasil_desimal']}")
        else:
            print(f"❌ Kesalahan: {hasil['error']}")
    
    def simulasi_kesalahan_interaktif(self):
        """Menu simulasi kesalahan interaktif"""
        print("\n⚠️  SIMULASI KESALAHAN")
        print("=" * 30)
        
        # Pilih sistem bilangan
        self.tampilkan_menu_sistem("Pilih sistem bilangan")
        sistem = self.pilih_sistem("Pilih sistem")
        if not sistem:
            return
        
        # Input nilai
        nilai = self.input_nilai(sistem)
        if not nilai:
            return
        
        # Pilih jenis kesalahan
        print("\nPilih jenis kesalahan yang akan disimulasikan:")
        print("1. 🔀 Bit Flip")
        print("2. 🔄 Salah Konversi")
        print("3. 🤔 Salah Interpretasi")
        print("4. 📈 Overflow")
        print("5. 📉 Underflow")
        
        kesalahan_map = {
            '1': JenisKesalahan.BIT_FLIP,
            '2': JenisKesalahan.SALAH_KONVERSI,
            '3': JenisKesalahan.SALAH_INTERPRETASI,
            '4': JenisKesalahan.OVERFLOW,
            '5': JenisKesalahan.UNDERFLOW
        }
        
        while True:
            pilihan = input("Pilih jenis kesalahan (1-5): ").strip()
            if pilihan in kesalahan_map:
                jenis_kesalahan = kesalahan_map[pilihan]
                break
            print("❌ Pilihan tidak valid.")
        
        # Simulasikan kesalahan
        try:
            hasil_error, penjelasan = self.konverter.simulasi_kesalahan(nilai, sistem, jenis_kesalahan)
            
            print(f"\n⚠️  HASIL SIMULASI KESALAHAN:")
            print(f"   Nilai asli: {nilai}")
            print(f"   Nilai dengan kesalahan: {hasil_error}")
            print(f"   Penjelasan: {penjelasan}")
            
            # Tampilkan dampak kesalahan jika berbeda
            if hasil_error != nilai:
                try:
                    nilai_desimal_asli = self.konverter.ke_desimal(nilai, sistem)
                    if self.konverter.validasi_input(hasil_error, sistem):
                        nilai_desimal_error = self.konverter.ke_desimal(hasil_error, sistem)
                        selisih = abs(nilai_desimal_error - nilai_desimal_asli)
                        print(f"   Dampak kesalahan: Selisih {selisih} dalam desimal")
                    else:
                        print(f"   Dampak kesalahan: Hasil tidak valid untuk sistem {sistem.value}")
                except:
                    print("   Dampak kesalahan: Tidak dapat dihitung")
            
        except Exception as e:
            print(f"❌ Kesalahan simulasi: {e}")
    
    def deteksi_kesalahan_interaktif(self):
        """Menu deteksi kesalahan interaktif"""
        print("\n🔍 DETEKSI KESALAHAN KONVERSI")
        print("=" * 35)
        
        # Pilih sistem asal
        self.tampilkan_menu_sistem("Pilih sistem bilangan ASAL")
        sistem_asal = self.pilih_sistem("Pilih sistem asal")
        if not sistem_asal:
            return
        
        # Input nilai asal
        nilai_asal = self.input_nilai(sistem_asal)
        if not nilai_asal:
            return
        
        # Pilih sistem tujuan
        self.tampilkan_menu_sistem("Pilih sistem bilangan TUJUAN")
        sistem_tujuan = self.pilih_sistem("Pilih sistem tujuan")
        if not sistem_tujuan:
            return
        
        # Input hasil konversi yang akan diperiksa
        print(f"\nMasukkan hasil konversi yang akan diperiksa dalam sistem {sistem_tujuan.value}:")
        hasil_input = input("Hasil konversi: ").strip()
        
        if sistem_tujuan == SistemBilangan.HEKSADESIMAL:
            hasil_input = hasil_input.upper()
        
        # Lakukan deteksi kesalahan
        try:
            analisis = self.konverter.deteksi_kesalahan_konversi(
                nilai_asal, hasil_input, sistem_asal, sistem_tujuan
            )
            
            print(f"\n🔍 HASIL ANALISIS KESALAHAN:")
            print(f"   Nilai asal ({sistem_asal.value}): {nilai_asal}")
            print(f"   Hasil input ({sistem_tujuan.value}): {hasil_input}")
            print(f"   Hasil yang benar: {analisis['hasil_benar']}")
            
            if analisis['ada_kesalahan']:
                print(f"   ❌ Status: KESALAHAN TERDETEKSI")
                print(f"   🎯 Tingkat kepercayaan: {analisis['tingkat_kepercayaan']:.1%}")
                print(f"   📝 Jenis kesalahan:")
                for kesalahan in analisis['jenis_kesalahan']:
                    print(f"      • {kesalahan}")
            else:
                print(f"   ✅ Status: KONVERSI BENAR")
                
        except Exception as e:
            print(f"❌ Kesalahan analisis: {e}")
    
    def tampilkan_riwayat(self):
        """Menampilkan riwayat konversi"""
        print("\n📜 RIWAYAT KONVERSI")
        print("=" * 25)
        
        if not self.konverter.riwayat_konversi:
            print("📭 Belum ada riwayat konversi.")
            return
        
        print(f"Total konversi: {len(self.konverter.riwayat_konversi)}")
        print("-" * 60)
        
        for i, entry in enumerate(self.konverter.riwayat_konversi[-10:], 1):  # Tampilkan 10 terakhir
            print(f"{i:2d}. {entry['nilai_asal']} ({entry['sistem_asal']}) → "
                  f"{entry['hasil']} ({entry['sistem_tujuan']}) "
                  f"[desimal: {entry['nilai_desimal']}]")
    
    def tampilkan_bantuan(self):
        """Menampilkan informasi bantuan"""
        print("\n❓ BANTUAN DAN INFORMASI")
        print("=" * 30)
        
        print("\n📚 SISTEM BILANGAN YANG DIDUKUNG:")
        print("   • Biner (Base-2): Menggunakan digit 0, 1")
        print("   • Desimal (Base-10): Menggunakan digit 0-9")
        print("   • Oktal (Base-8): Menggunakan digit 0-7")
        print("   • Heksadesimal (Base-16): Menggunakan digit 0-9, A-F")
        
        print("\n🔧 FITUR PROGRAM:")
        print("   • Konversi akurat antar semua sistem bilangan")
        print("   • Operasi aritmatika dalam sistem bilangan apapun")
        print("   • Simulasi berbagai jenis kesalahan")
        print("   • Deteksi kesalahan dalam hasil konversi")
        print("   • Validasi input yang ketat")
        print("   • Riwayat konversi")
        
        print("\n⚠️  JENIS KESALAHAN YANG DAPAT DISIMULASIKAN:")
        print("   • Bit Flip: Perubahan bit acak (0→1 atau 1→0)")
        print("   • Salah Konversi: Kesalahan dalam proses konversi")
        print("   • Salah Interpretasi: Salah mengidentifikasi sistem bilangan")
        print("   • Overflow: Nilai melebihi kapasitas")
        print("   • Underflow: Nilai kurang dari minimum")
        
        print("\n💡 TIPS PENGGUNAAN:")
        print("   • Gunakan huruf kapital untuk heksadesimal (A-F)")
        print("   • Program hanya mendukung bilangan positif")
        print("   • Tekan Ctrl+C kapan saja untuk kembali ke menu")
        print("   • Masukkan 0 untuk kembali ke menu sebelumnya")
    
    def jalankan(self):
        """Menjalankan program utama"""
        self.tampilkan_header()
        
        while True:
            try:
                self.tampilkan_menu_utama()
                pilihan = input("Masukkan pilihan Anda (1-8): ").strip()
                
                if pilihan == '1':
                    self.konversi_interaktif()
                elif pilihan == '2':
                    self.tabel_konversi_lengkap()
                elif pilihan == '3':
                    self.operasi_aritmatika_interaktif()
                elif pilihan == '4':
                    self.simulasi_kesalahan_interaktif()
                elif pilihan == '5':
                    self.deteksi_kesalahan_interaktif()
                elif pilihan == '6':
                    self.tampilkan_riwayat()
                elif pilihan == '7':
                    self.tampilkan_bantuan()
                elif pilihan == '8':
                    print("\n👋 Terima kasih telah menggunakan Simulator Sistem Bilangan!")
                    print("🎓 Semoga program ini membantu Anda memahami sistem bilangan dengan lebih baik.")
                    break
                else:
                    print("❌ Pilihan tidak valid. Silakan pilih 1-8.")
                
                # Jeda sebelum kembali ke menu
                if pilihan in ['1', '2', '3', '4', '5', '6', '7']:
                    input("\n⏸️  Tekan Enter untuk kembali ke menu utama...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program dihentikan oleh pengguna.")
                print("🎓 Terima kasih telah menggunakan Simulator Sistem Bilangan!")
                break
            except Exception as e:
                print(f"\n❌ Terjadi kesalahan tidak terduga: {e}")
                print("🔄 Kembali ke menu utama...")


def demo_otomatis():
    """
    Demonstrasi otomatis fitur-fitur program
    Berguna untuk testing dan showcase
    """
    print("\n🎬 DEMONSTRASI OTOMATIS")
    print("=" * 30)
    
    konverter = KonverterSistemBilangan()
    
    # Demo konversi dasar
    print("\n1️⃣  Demo Konversi Dasar:")
    nilai_demo = "42"
    sistem_asal = SistemBilangan.DESIMAL
    
    print(f"   Nilai asal: {nilai_demo} ({sistem_asal.value})")
    
    for sistem_tujuan in SistemBilangan:
        if sistem_tujuan != sistem_asal:
            try:
                hasil = konverter.konversi(nilai_demo, sistem_asal, sistem_tujuan)
                print(f"   → {sistem_tujuan.value}: {hasil}")
            except Exception as e:
                print(f"   → {sistem_tujuan.value}: Error - {e}")
    
    # Demo simulasi kesalahan
    print("\n2️⃣  Demo Simulasi Kesalahan:")
    nilai_biner = "1010101"
    
    for jenis in JenisKesalahan:
        try:
            hasil_error, penjelasan = konverter.simulasi_kesalahan(
                nilai_biner, SistemBilangan.BINER, jenis
            )
            print(f"   {jenis.value}: {nilai_biner} → {hasil_error}")
            print(f"      {penjelasan}")
        except Exception as e:
            print(f"   {jenis.value}: Error - {e}")
    
    # Demo operasi aritmatika
    print("\n3️⃣  Demo Operasi Aritmatika:")
    hasil_op = konverter.operasi_aritmatika("1010", "110", "+", SistemBilangan.BINER)
    if hasil_op['berhasil']:
        print(f"   {hasil_op['operasi']} = {hasil_op['hasil_sistem']} (biner)")
        print(f"   Dalam desimal: {hasil_op['hasil_desimal']}")
    
    print("\n✅ Demo selesai!")


if __name__ == "__main__":
    """
    Fungsi main untuk menjalankan program
    
    Program dapat dijalankan dalam dua mode:
    1. Mode interaktif (default): Interface pengguna lengkap
    2. Mode demo: Demonstrasi otomatis fitur-fitur program
    """
    
    print("🚀 Memulai Simulator Sistem Bilangan...")
    
    # Tanya pengguna apakah ingin menjalankan demo atau mode interaktif
    try:
        mode = input("\nPilih mode:\n1. 🎮 Mode Interaktif\n2. 🎬 Demo Otomatis\nPilihan (1/2): ").strip()
        
        if mode == '2':
            demo_otomatis()
            print("\n" + "="*50)
            print("Demo selesai. Memulai mode interaktif...")
            input("Tekan Enter untuk melanjutkan...")
        
        # Jalankan mode interaktif
        interface = InterfacePengguna()
        interface.jalankan()
        
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh pengguna.")
        print("🎓 Terima kasih!")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan fatal: {e}")
        print("🔄 Silakan restart program.")
