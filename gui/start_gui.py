#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk menjalankan GUI Simulator Sistem Bilangan
======================================================

Script ini memudahkan pengguna untuk menjalankan GUI dengan berbagai opsi.

Penggunaan:
    python start_gui.py          # GUI standar
    python start_gui.py --demo   # GUI dengan demo
    python start_gui.py --test   # Jalankan test
    python start_gui.py --help   # Bantuan
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path


def check_requirements():
    """Memeriksa apakah semua file yang diperlukan tersedia"""
    required_files = [
        'gui_simulator.py',
        'number_system_simulator.py',
        'demo_gui.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ File yang tidak ditemukan: {', '.join(missing_files)}")
        return False
    
    return True


def run_gui(demo_mode=False):
    """Menjalankan GUI"""
    if not check_requirements():
        return False
    
    try:
        if demo_mode:
            print("🎬 Menjalankan GUI dengan fitur demo...")
            subprocess.run([sys.executable, 'demo_gui.py'])
        else:
            print("🖥️ Menjalankan GUI standar...")
            subprocess.run([sys.executable, 'gui_simulator.py'])
        
        return True
    except KeyboardInterrupt:
        print("\n👋 GUI dihentikan oleh pengguna.")
        return True
    except Exception as e:
        print(f"❌ Error menjalankan GUI: {e}")
        return False


def run_tests():
    """Menjalankan test suite"""
    print("🧪 Menjalankan test suite...")
    
    try:
        result = subprocess.run([sys.executable, 'run_all_tests.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Semua test berhasil!")
            print(result.stdout)
        else:
            print("❌ Beberapa test gagal!")
            print(result.stderr)
            print(result.stdout)
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error menjalankan test: {e}")
        return False


def show_help():
    """Menampilkan bantuan"""
    help_text = """
🔢 GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan

PENGGUNAAN:
    python start_gui.py          # Menjalankan GUI standar
    python start_gui.py --demo   # Menjalankan GUI dengan fitur demo
    python start_gui.py --test   # Menjalankan test suite
    python start_gui.py --help   # Menampilkan bantuan ini

FITUR GUI:
    🔄 Konversi antar sistem bilangan (biner, desimal, oktal, heksadesimal)
    🧮 Operasi aritmatika dalam berbagai sistem
    ⚠️ Simulasi berbagai jenis kesalahan
    🔍 Deteksi kesalahan dalam konversi
    📜 Riwayat konversi
    ❓ Bantuan lengkap

CONTOH PENGGUNAAN:
    1. Jalankan: python start_gui.py
    2. Pilih tab "Konversi"
    3. Masukkan nilai dan pilih sistem
    4. Klik "Konversi" untuk melihat hasil

FILE YANG DIPERLUKAN:
    - gui_simulator.py (GUI utama)
    - number_system_simulator.py (Engine konversi)
    - demo_gui.py (GUI dengan demo, opsional)

PERSYARATAN:
    - Python 3.6+
    - Tkinter (biasanya sudah terinstall dengan Python)

TROUBLESHOOTING:
    - Jika GUI tidak terbuka, periksa apakah tkinter terinstall
    - Pastikan semua file ada di direktori yang sama
    - Jalankan test: python start_gui.py --test

🎓 Selamat menggunakan Simulator Sistem Bilangan!
    """
    print(help_text)


def main():
    """Fungsi main"""
    parser = argparse.ArgumentParser(
        description='GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--demo', 
        action='store_true', 
        help='Menjalankan GUI dengan fitur demo'
    )
    
    parser.add_argument(
        '--test', 
        action='store_true', 
        help='Menjalankan test suite'
    )
    
    parser.add_argument(
        '--help-extended', 
        action='store_true', 
        help='Menampilkan bantuan lengkap'
    )
    
    args = parser.parse_args()
    
    print("🔢 GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan")
    print("=" * 60)
    
    if args.help_extended:
        show_help()
        return True
    
    if args.test:
        success = run_tests()
        if success:
            print("\n🎉 Test berhasil! GUI siap digunakan.")
        else:
            print("\n⚠️ Beberapa test gagal. Periksa error di atas.")
        return success
    
    # Jalankan GUI
    success = run_gui(demo_mode=args.demo)
    
    if success:
        print("\n🎉 Terima kasih telah menggunakan Simulator Sistem Bilangan!")
    else:
        print("\n❌ Terjadi masalah saat menjalankan GUI.")
        print("💡 Coba jalankan: python start_gui.py --help")
    
    return success


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh pengguna.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error tidak terduga: {e}")
        sys.exit(1)
