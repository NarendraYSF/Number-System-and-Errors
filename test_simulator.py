#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script untuk Simulator Sistem Bilangan
"""

from number_system_simulator import KonverterSistemBilangan, SistemBilangan, JenisKesalahan

def test_konversi_dasar():
    """Test konversi dasar antar sistem bilangan"""
    print("🧪 Testing konversi dasar...")
    
    konverter = KonverterSistemBilangan()
    
    # Test konversi desimal ke sistem lain
    nilai = "42"
    sistem_asal = SistemBilangan.DESIMAL
    
    print(f"Nilai asal: {nilai} ({sistem_asal.value})")
    
    for sistem_tujuan in SistemBilangan:
        if sistem_tujuan != sistem_asal:
            try:
                hasil = konverter.konversi(nilai, sistem_asal, sistem_tujuan)
                print(f"  → {sistem_tujuan.value}: {hasil}")
            except Exception as e:
                print(f"  → {sistem_tujuan.value}: ERROR - {e}")
    
    print("✅ Test konversi dasar selesai\n")

def test_validasi_input():
    """Test validasi input"""
    print("🧪 Testing validasi input...")
    
    konverter = KonverterSistemBilangan()
    
    test_cases = [
        ("101010", SistemBilangan.BINER, True),
        ("102010", SistemBilangan.BINER, False),
        ("123", SistemBilangan.DESIMAL, True),
        ("12A", SistemBilangan.DESIMAL, False),
        ("777", SistemBilangan.OKTAL, True),
        ("789", SistemBilangan.OKTAL, False),
        ("ABC", SistemBilangan.HEKSADESIMAL, True),
        ("XYZ", SistemBilangan.HEKSADESIMAL, False),
    ]
    
    for nilai, sistem, expected in test_cases:
        hasil = konverter.validasi_input(nilai, sistem)
        status = "✅" if hasil == expected else "❌"
        print(f"  {status} {nilai} pada {sistem.value}: {hasil} (expected: {expected})")
    
    print("✅ Test validasi input selesai\n")

def test_simulasi_kesalahan():
    """Test simulasi kesalahan"""
    print("🧪 Testing simulasi kesalahan...")
    
    konverter = KonverterSistemBilangan()
    nilai = "1010101"
    sistem = SistemBilangan.BINER
    
    print(f"Nilai asal: {nilai} ({sistem.value})")
    
    for jenis in JenisKesalahan:
        try:
            hasil_error, penjelasan = konverter.simulasi_kesalahan(nilai, sistem, jenis)
            print(f"  {jenis.value}: {hasil_error}")
            print(f"    Penjelasan: {penjelasan}")
        except Exception as e:
            print(f"  {jenis.value}: ERROR - {e}")
    
    print("✅ Test simulasi kesalahan selesai\n")

def test_operasi_aritmatika():
    """Test operasi aritmatika"""
    print("🧪 Testing operasi aritmatika...")
    
    konverter = KonverterSistemBilangan()
    
    test_cases = [
        ("1010", "110", "+", SistemBilangan.BINER),
        ("FF", "1", "+", SistemBilangan.HEKSADESIMAL),
        ("77", "7", "*", SistemBilangan.OKTAL),
        ("100", "25", "/", SistemBilangan.DESIMAL),
    ]
    
    for nilai1, nilai2, operasi, sistem in test_cases:
        hasil = konverter.operasi_aritmatika(nilai1, nilai2, operasi, sistem)
        if hasil['berhasil']:
            print(f"  ✅ {nilai1} {operasi} {nilai2} = {hasil['hasil_sistem']} ({sistem.value})")
            print(f"     Desimal: {hasil['hasil_desimal']}")
        else:
            print(f"  ❌ {nilai1} {operasi} {nilai2}: {hasil['error']}")
    
    print("✅ Test operasi aritmatika selesai\n")

if __name__ == "__main__":
    print("🚀 Menjalankan test suite untuk Simulator Sistem Bilangan...\n")
    
    test_konversi_dasar()
    test_validasi_input()
    test_simulasi_kesalahan()
    test_operasi_aritmatika()
    
    print("🎉 Semua test selesai!")
    print("\nUntuk menjalankan program utama, jalankan: python number_system_simulator.py")
