#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk menjalankan semua test suite
=========================================

Script ini menjalankan semua test untuk memastikan aplikasi berfungsi dengan baik.

Test yang dijalankan:
- Test engine konversi (test_simulator.py)
- Test GUI (test_gui.py)
- Test integrasi

Penulis: AI Assistant
Tanggal: 2024
"""

import subprocess
import sys
import os
import time
from datetime import datetime


def run_test_file(test_file, description):
    """Menjalankan file test tertentu"""
    print(f"\n🧪 {description}")
    print("=" * 50)
    
    if not os.path.exists(test_file):
        print(f"❌ File {test_file} tidak ditemukan!")
        return False
    
    try:
        start_time = time.time()
        result = subprocess.run([sys.executable, test_file], 
                              capture_output=True, text=True, timeout=60)
        end_time = time.time()
        
        duration = end_time - start_time
        
        if result.returncode == 0:
            print(f"✅ {description} BERHASIL")
            print(f"⏱️ Waktu: {duration:.2f} detik")
            if result.stdout:
                print("📝 Output:")
                print(result.stdout)
            return True
        else:
            print(f"❌ {description} GAGAL")
            print(f"⏱️ Waktu: {duration:.2f} detik")
            if result.stderr:
                print("💥 Error:")
                print(result.stderr)
            if result.stdout:
                print("📝 Output:")
                print(result.stdout)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {description} TIMEOUT (lebih dari 60 detik)")
        return False
    except Exception as e:
        print(f"💥 Error menjalankan {description}: {e}")
        return False


def check_dependencies():
    """Memeriksa dependency yang diperlukan"""
    print("🔍 Memeriksa dependency...")
    
    # Periksa Python version
    python_version = sys.version_info
    if python_version < (3, 6):
        print(f"❌ Python {python_version.major}.{python_version.minor} tidak didukung. Minimal Python 3.6")
        return False
    else:
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Periksa tkinter
    try:
        import tkinter
        print("✅ Tkinter tersedia")
    except ImportError:
        print("❌ Tkinter tidak tersedia")
        return False
    
    # Periksa file yang diperlukan
    required_files = [
        'number_system_simulator.py',
        'test_simulator.py',
        'gui_simulator.py',
        'test_gui.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file}")
    
    if missing_files:
        print(f"❌ File yang tidak ditemukan: {', '.join(missing_files)}")
        return False
    
    return True


def run_all_tests():
    """Menjalankan semua test suite"""
    print("🚀 MENJALANKAN SEMUA TEST SUITE")
    print("=" * 50)
    print(f"📅 Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python: {sys.version}")
    print(f"📁 Direktori: {os.getcwd()}")
    
    # Periksa dependency
    if not check_dependencies():
        print("\n❌ Dependency tidak lengkap. Test dibatalkan.")
        return False
    
    # Daftar test yang akan dijalankan
    tests = [
        ('test_simulator.py', 'Test Engine Konversi'),
        ('test_gui.py', 'Test GUI Simulator'),
    ]
    
    # Jalankan test
    results = []
    total_tests = len(tests)
    passed_tests = 0
    
    for test_file, description in tests:
        success = run_test_file(test_file, description)
        results.append((description, success))
        if success:
            passed_tests += 1
    
    # Tampilkan ringkasan
    print("\n" + "=" * 50)
    print("📊 RINGKASAN HASIL TEST")
    print("=" * 50)
    
    for description, success in results:
        status = "✅ BERHASIL" if success else "❌ GAGAL"
        print(f"  {description}: {status}")
    
    print(f"\n📈 Total: {passed_tests}/{total_tests} test berhasil")
    
    if passed_tests == total_tests:
        print("🎉 SEMUA TEST BERHASIL!")
        print("✅ Aplikasi siap digunakan.")
        return True
    else:
        print("⚠️ BEBERAPA TEST GAGAL!")
        print("🔧 Periksa error di atas dan perbaiki sebelum menggunakan aplikasi.")
        return False


def main():
    """Fungsi main"""
    try:
        success = run_all_tests()
        
        if success:
            print("\n🎯 REKOMENDASI:")
            print("  • Jalankan GUI: python gui_simulator.py")
            print("  • Jalankan demo: python demo_gui.py")
            print("  • Jalankan CLI: python number_system_simulator.py")
        else:
            print("\n🔧 TROUBLESHOOTING:")
            print("  • Periksa error di atas")
            print("  • Pastikan semua file tersedia")
            print("  • Pastikan Python 3.6+ terinstall")
            print("  • Pastikan tkinter tersedia")
        
        return success
        
    except KeyboardInterrupt:
        print("\n\n👋 Test dihentikan oleh pengguna.")
        return False
    except Exception as e:
        print(f"\n💥 Error tidak terduga: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
