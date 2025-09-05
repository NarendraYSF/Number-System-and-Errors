#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulator Sistem Bilangan Sederhana
===================================

Versi sederhana dari simulator sistem bilangan tanpa GUI.
Menyediakan fungsi-fitur inti untuk konversi antar sistem bilangan.

Fitur:
- Konversi antar sistem bilangan (biner, desimal, oktal, heksadesimal)
- Validasi input yang kuat
- Interface command-line sederhana
- Operasi aritmatika dasar

Penulis: Kelompok 1
Tanggal: 5/9/2025
"""

import re
from typing import Dict, List, Tuple, Optional
from enum import Enum


class SistemBilangan(Enum):
    """Enumerasi untuk berbagai sistem bilangan yang didukung"""
    BINER = "biner"
    DESIMAL = "desimal"
    HEKSADESIMAL = "heksadesimal"
    OKTAL = "oktal"


class KonverterSistemBilangan:
    """
    Kelas utama untuk konversi antar sistem bilangan
    
    Kelas ini menyediakan metode untuk:
    - Konversi antar berbagai sistem bilangan
    - Validasi input
    - Operasi aritmatika dasar
    """
    
    def __init__(self):
        """Inisialisasi konverter dengan konfigurasi default"""
        self.riwayat_konversi: List[Dict] = []
        
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


class SimpleInterface:
    """
    Interface sederhana untuk interaksi dengan pengguna
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
        print("=" * 60)
        print("🔢 SIMULATOR SISTEM BILANGAN SEDERHANA 🔢")
        print("=" * 60)
        print("Program untuk konversi antar sistem bilangan")
        print("=" * 60)
    
    def tampilkan_menu(self):
        """Menampilkan menu utama"""
        print("\n📋 MENU:")
        print("1. 🔄 Konversi Antar Sistem Bilangan")
        print("2. 📊 Tabel Konversi Lengkap")
        print("3. 🧮 Operasi Aritmatika")
        print("4. 📜 Lihat Riwayat Konversi")
        print("5. ❓ Bantuan")
        print("6. 🚪 Keluar")
        print("-" * 40)
    
    def tampilkan_menu_sistem(self, judul: str = "Pilih Sistem Bilangan"):
        """Menampilkan menu pemilihan sistem bilangan"""
        print(f"\n{judul}:")
        print("1. 🔢 Biner (Binary)")
        print("2. 🔟 Desimal (Decimal)")
        print("3. 8️⃣  Oktal (Octal)")
        print("4. 🔠 Heksadesimal (Hexadecimal)")
    
    def pilih_sistem(self, prompt: str = "Masukkan pilihan sistem") -> Optional[SistemBilangan]:
        """Meminta pengguna memilih sistem bilangan"""
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
        """Meminta input nilai dari pengguna dengan validasi"""
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
        print("   • Validasi input yang ketat")
        print("   • Riwayat konversi")
        
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
                self.tampilkan_menu()
                pilihan = input("Masukkan pilihan Anda (1-6): ").strip()
                
                if pilihan == '1':
                    self.konversi_interaktif()
                elif pilihan == '2':
                    self.tabel_konversi_lengkap()
                elif pilihan == '3':
                    self.operasi_aritmatika_interaktif()
                elif pilihan == '4':
                    self.tampilkan_riwayat()
                elif pilihan == '5':
                    self.tampilkan_bantuan()
                elif pilihan == '6':
                    print("\n👋 Terima kasih telah menggunakan Simulator Sistem Bilangan!")
                    break
                else:
                    print("❌ Pilihan tidak valid. Silakan pilih 1-6.")
                
                # Jeda sebelum kembali ke menu
                if pilihan in ['1', '2', '3', '4', '5']:
                    input("\n⏸️  Tekan Enter untuk kembali ke menu utama...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program dihentikan oleh pengguna.")
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
    
    # Demo operasi aritmatika
    print("\n2️⃣  Demo Operasi Aritmatika:")
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
    
    print("🚀 Memulai Simulator Sistem Bilangan Sederhana...")
    
    # Tanya pengguna apakah ingin menjalankan demo atau mode interaktif
    try:
        mode = input("\nPilih mode:\n1. 🎮 Mode Interaktif\n2. 🎬 Demo Otomatis\nPilihan (1/2): ").strip()
        
        if mode == '2':
            demo_otomatis()
            print("\n" + "="*50)
            print("Demo selesai. Memulai mode interaktif...")
            input("Tekan Enter untuk melanjutkan...")
        
        # Jalankan mode interaktif
        interface = SimpleInterface()
        interface.jalankan()
        
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh pengguna.")
        print("🎓 Terima kasih!")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan fatal: {e}")
        print("🔄 Silakan restart program.")
