#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contoh Penggunaan Simulator Sistem Bilangan
==========================================

Script ini menunjukkan cara menggunakan berbagai fitur dari
Simulator Sistem Bilangan secara programatis.
"""

from number_system_simulator import KonverterSistemBilangan, SistemBilangan, JenisKesalahan

def contoh_konversi_dasar():
    """Contoh konversi dasar antar sistem bilangan"""
    print("📝 CONTOH 1: KONVERSI DASAR")
    print("-" * 30)
    
    konverter = KonverterSistemBilangan()
    
    # Konversi desimal ke sistem lain
    nilai = "42"
    sistem_asal = SistemBilangan.DESIMAL
    
    print(f"Nilai asal: {nilai} ({sistem_asal.value})")
    
    for sistem_tujuan in SistemBilangan:
        if sistem_tujuan != sistem_asal:
            hasil = konverter.konversi(nilai, sistem_asal, sistem_tujuan)
            print(f"  → {sistem_tujuan.value}: {hasil}")

def contoh_operasi_aritmatika():
    """Contoh operasi aritmatika dalam berbagai sistem"""
    print("\n📝 CONTOH 2: OPERASI ARITMATIKA")
    print("-" * 35)
    
    konverter = KonverterSistemBilangan()
    
    # Operasi dalam biner
    print("Operasi dalam sistem biner:")
    hasil = konverter.operasi_aritmatika("1010", "110", "+", SistemBilangan.BINER)
    if hasil['berhasil']:
        print(f"  1010 + 110 = {hasil['hasil_sistem']} (biner)")
        print(f"  Dalam desimal: 10 + 6 = {hasil['hasil_desimal']}")
    
    # Operasi dalam heksadesimal
    print("\nOperasi dalam sistem heksadesimal:")
    hasil = konverter.operasi_aritmatika("FF", "1", "+", SistemBilangan.HEKSADESIMAL)
    if hasil['berhasil']:
        print(f"  FF + 1 = {hasil['hasil_sistem']} (heksadesimal)")
        print(f"  Dalam desimal: 255 + 1 = {hasil['hasil_desimal']}")

def contoh_simulasi_kesalahan():
    """Contoh simulasi berbagai jenis kesalahan"""
    print("\n📝 CONTOH 3: SIMULASI KESALAHAN")
    print("-" * 30)
    
    konverter = KonverterSistemBilangan()
    nilai = "1010101"
    sistem = SistemBilangan.BINER
    
    print(f"Nilai asal: {nilai} ({sistem.value})")
    print(f"Nilai desimal: {konverter.ke_desimal(nilai, sistem)}")
    
    # Simulasi bit flip
    hasil_error, penjelasan = konverter.simulasi_kesalahan(nilai, sistem, JenisKesalahan.BIT_FLIP)
    print(f"\nBit Flip:")
    print(f"  Hasil: {hasil_error}")
    print(f"  Penjelasan: {penjelasan}")
    
    # Simulasi salah konversi
    hasil_error, penjelasan = konverter.simulasi_kesalahan(nilai, sistem, JenisKesalahan.SALAH_KONVERSI)
    print(f"\nSalah Konversi:")
    print(f"  Hasil: {hasil_error}")
    print(f"  Penjelasan: {penjelasan}")

def contoh_deteksi_kesalahan():
    """Contoh deteksi kesalahan dalam konversi"""
    print("\n📝 CONTOH 4: DETEKSI KESALAHAN")
    print("-" * 30)
    
    konverter = KonverterSistemBilangan()
    
    # Test dengan konversi yang benar
    print("Test 1 - Konversi yang benar:")
    analisis = konverter.deteksi_kesalahan_konversi(
        "42", "101010", SistemBilangan.DESIMAL, SistemBilangan.BINER
    )
    
    print(f"  42 (desimal) → 101010 (biner)")
    print(f"  Status: {'✅ BENAR' if not analisis['ada_kesalahan'] else '❌ SALAH'}")
    
    # Test dengan konversi yang salah
    print("\nTest 2 - Konversi yang salah:")
    analisis = konverter.deteksi_kesalahan_konversi(
        "42", "101011", SistemBilangan.DESIMAL, SistemBilangan.BINER
    )
    
    print(f"  42 (desimal) → 101011 (biner)")
    print(f"  Status: {'✅ BENAR' if not analisis['ada_kesalahan'] else '❌ SALAH'}")
    
    if analisis['ada_kesalahan']:
        print(f"  Hasil yang benar: {analisis['hasil_benar']}")
        print(f"  Tingkat kepercayaan: {analisis['tingkat_kepercayaan']:.1%}")
        if analisis['jenis_kesalahan']:
            print(f"  Jenis kesalahan: {', '.join(analisis['jenis_kesalahan'])}")

def contoh_validasi_input():
    """Contoh validasi input"""
    print("\n📝 CONTOH 5: VALIDASI INPUT")
    print("-" * 25)
    
    konverter = KonverterSistemBilangan()
    
    test_cases = [
        ("101010", SistemBilangan.BINER),
        ("102010", SistemBilangan.BINER),  # Invalid - ada digit 2
        ("ABC", SistemBilangan.HEKSADESIMAL),
        ("XYZ", SistemBilangan.HEKSADESIMAL),  # Invalid - huruf tidak valid
    ]
    
    for nilai, sistem in test_cases:
        valid = konverter.validasi_input(nilai, sistem)
        status = "✅ VALID" if valid else "❌ INVALID"
        print(f"  '{nilai}' untuk {sistem.value}: {status}")

def main():
    """Menjalankan semua contoh"""
    print("🎓 CONTOH PENGGUNAAN SIMULATOR SISTEM BILANGAN")
    print("=" * 50)
    print("Script ini menunjukkan cara menggunakan semua fitur program.")
    print("=" * 50)
    
    contoh_konversi_dasar()
    contoh_operasi_aritmatika()
    contoh_simulasi_kesalahan()
    contoh_deteksi_kesalahan()
    contoh_validasi_input()
    
    print("\n" + "=" * 50)
    print("🎉 SEMUA CONTOH SELESAI!")
    print("🎮 Untuk pengalaman interaktif, jalankan: python number_system_simulator.py")
    print("🧪 Untuk menjalankan test: python test_simulator.py")
    print("🎬 Untuk demo dengan animasi: python demo.py")

if __name__ == "__main__":
    main()
