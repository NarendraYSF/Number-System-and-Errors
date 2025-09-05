#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk menjalankan GUI Simulator Sistem Bilangan
======================================================

Script ini memudahkan pengguna untuk menjalankan GUI dengan berbagai opsi.

Penggunaan:
    python run_gui.py          # GUI standar
    python run_gui.py --demo   # GUI dengan demo
    python run_gui.py --help   # Bantuan
"""

import sys
import argparse
import subprocess
import os


def check_dependencies():
    """Memeriksa apakah semua dependency tersedia"""
    try:
        import tkinter
        print("✅ Tkinter tersedia")
    except ImportError:
        print("❌ Tkinter tidak tersedia. Install dengan: pip install tk")
        return False
    
    # Periksa file yang diperlukan
    required_files = [
        'gui_simulator.py',
        'number_system_simulator.py'
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ File {file} tidak ditemukan")
            return False
        else:
            print(f"✅ File {file} tersedia")
    
    return True


def run_gui(demo_mode=False):
    """Menjalankan GUI"""
    if not check_dependencies():
        print("\n❌ Tidak dapat menjalankan GUI. Periksa dependency di atas.")
        return False
    
    try:
        if demo_mode:
            print("\n🎬 Menjalankan GUI dengan fitur demo...")
            subprocess.run([sys.executable, 'demo_gui.py'])
        else:
            print("\n🖥️ Menjalankan GUI standar...")
            subprocess.run([sys.executable, 'gui_simulator.py'])
        
        print("\n✅ GUI selesai dijalankan.")
        return True
        
    except KeyboardInterrupt:
        print("\n\n👋 GUI dihentikan oleh pengguna.")
        return True
    except Exception as e:
        print(f"\n❌ Error menjalankan GUI: {e}")
        return False


def show_help():
    """Menampilkan bantuan"""
    help_text = """
🔢 GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan

PENGGUNAAN:
    python run_gui.py          # Menjalankan GUI standar
    python run_gui.py --demo   # Menjalankan GUI dengan fitur demo
    python run_gui.py --help   # Menampilkan bantuan ini

FITUR GUI:
    🔄 Konversi antar sistem bilangan (biner, desimal, oktal, heksadesimal)
    🧮 Operasi aritmatika dalam berbagai sistem
    ⚠️ Simulasi berbagai jenis kesalahan
    🔍 Deteksi kesalahan dalam konversi
    📜 Riwayat konversi
    ❓ Bantuan lengkap

CONTOH PENGGUNAAN:
    1. Jalankan: python run_gui.py
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
    - Jalankan test: python test_simulator.py

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
        '--help-extended', 
        action='store_true', 
        help='Menampilkan bantuan lengkap'
    )
    
    args = parser.parse_args()
    
    if args.help_extended:
        show_help()
        return
    
    print("🔢 GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan")
    print("=" * 60)
    
    success = run_gui(demo_mode=args.demo)
    
    if success:
        print("\n🎉 Terima kasih telah menggunakan Simulator Sistem Bilangan!")
    else:
        print("\n❌ Terjadi masalah saat menjalankan GUI.")
        print("💡 Coba jalankan: python run_gui.py --help")


if __name__ == "__main__":
    main()
