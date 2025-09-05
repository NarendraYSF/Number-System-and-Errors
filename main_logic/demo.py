#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Script untuk Simulator Sistem Bilangan
Menunjukkan berbagai fitur program secara otomatis
"""

from number_system_simulator import KonverterSistemBilangan, SistemBilangan, JenisKesalahan
import time

def demo_dengan_jeda(detik=1.5):
    """Memberikan jeda untuk demo yang lebih mudah diikuti"""
    time.sleep(detik)

def demo_konversi():
    """Demo konversi antar sistem bilangan"""
    print("🎬 DEMO 1: KONVERSI ANTAR SISTEM BILANGAN")
    print("=" * 45)
    
    konverter = KonverterSistemBilangan()
    
    # Demo dengan berbagai nilai
    demo_values = [
        ("42", SistemBilangan.DESIMAL),
        ("101010", SistemBilangan.BINER),
        ("2A", SistemBilangan.HEKSADESIMAL),
        ("52", SistemBilangan.OKTAL)
    ]
    
    for nilai, sistem_asal in demo_values:
        print(f"\n📍 Konversi dari {nilai} ({sistem_asal.value}):")
        demo_dengan_jeda()
        
        hasil_tabel = konverter.tampilkan_tabel_konversi(nilai, sistem_asal)
        
        for sistem, hasil in hasil_tabel.items():
            if sistem != 'error':
                print(f"   → {sistem.capitalize():<12}: {hasil}")
                demo_dengan_jeda(0.3)

def demo_operasi_aritmatika():
    """Demo operasi aritmatika"""
    print("\n\n🎬 DEMO 2: OPERASI ARITMATIKA")
    print("=" * 35)
    
    konverter = KonverterSistemBilangan()
    
    operasi_demo = [
        ("1010", "110", "+", SistemBilangan.BINER, "Penjumlahan biner"),
        ("FF", "1", "+", SistemBilangan.HEKSADESIMAL, "Penjumlahan heksadesimal"),
        ("100", "25", "*", SistemBilangan.DESIMAL, "Perkalian desimal"),
        ("77", "7", "-", SistemBilangan.OKTAL, "Pengurangan oktal"),
    ]
    
    for nilai1, nilai2, op, sistem, deskripsi in operasi_demo:
        print(f"\n📍 {deskripsi}:")
        demo_dengan_jeda()
        
        hasil = konverter.operasi_aritmatika(nilai1, nilai2, op, sistem)
        
        if hasil['berhasil']:
            print(f"   {nilai1} {op} {nilai2} = {hasil['hasil_sistem']} ({sistem.value})")
            print(f"   Dalam desimal: {hasil['hasil_desimal']}")
        else:
            print(f"   ❌ Error: {hasil['error']}")
        
        demo_dengan_jeda()

def demo_simulasi_kesalahan():
    """Demo simulasi berbagai jenis kesalahan"""
    print("\n\n🎬 DEMO 3: SIMULASI KESALAHAN")
    print("=" * 30)
    
    konverter = KonverterSistemBilangan()
    nilai_demo = "1010101"
    sistem = SistemBilangan.BINER
    
    print(f"\n📍 Nilai asal: {nilai_demo} ({sistem.value})")
    print(f"   Nilai desimal: {konverter.ke_desimal(nilai_demo, sistem)}")
    
    demo_dengan_jeda()
    
    for jenis in JenisKesalahan:
        print(f"\n🔸 Simulasi {jenis.value.replace('_', ' ').title()}:")
        demo_dengan_jeda()
        
        try:
            hasil_error, penjelasan = konverter.simulasi_kesalahan(nilai_demo, sistem, jenis)
            print(f"   Hasil: {hasil_error}")
            print(f"   Penjelasan: {penjelasan}")
            
            # Hitung dampak kesalahan jika memungkinkan
            if hasil_error != nilai_demo and konverter.validasi_input(hasil_error, sistem):
                try:
                    nilai_asli = konverter.ke_desimal(nilai_demo, sistem)
                    nilai_error = konverter.ke_desimal(hasil_error, sistem)
                    selisih = abs(nilai_error - nilai_asli)
                    print(f"   Dampak: Selisih {selisih} dalam desimal")
                except:
                    pass
                    
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        demo_dengan_jeda()

def demo_deteksi_kesalahan():
    """Demo deteksi kesalahan"""
    print("\n\n🎬 DEMO 4: DETEKSI KESALAHAN")
    print("=" * 30)
    
    konverter = KonverterSistemBilangan()
    
    # Test cases dengan hasil yang benar dan salah
    test_cases = [
        ("42", "101010", SistemBilangan.DESIMAL, SistemBilangan.BINER, "Konversi Benar"),
        ("42", "101011", SistemBilangan.DESIMAL, SistemBilangan.BINER, "Konversi Salah (1 bit)"),
        ("FF", "255", SistemBilangan.HEKSADESIMAL, SistemBilangan.DESIMAL, "Konversi Benar"),
        ("FF", "256", SistemBilangan.HEKSADESIMAL, SistemBilangan.DESIMAL, "Konversi Salah"),
    ]
    
    for nilai_asal, hasil_input, sistem_asal, sistem_tujuan, deskripsi in test_cases:
        print(f"\n📍 {deskripsi}:")
        print(f"   {nilai_asal} ({sistem_asal.value}) → {hasil_input} ({sistem_tujuan.value})")
        demo_dengan_jeda()
        
        analisis = konverter.deteksi_kesalahan_konversi(
            nilai_asal, hasil_input, sistem_asal, sistem_tujuan
        )
        
        if analisis['ada_kesalahan']:
            print(f"   ❌ KESALAHAN TERDETEKSI")
            print(f"   📊 Tingkat kepercayaan: {analisis['tingkat_kepercayaan']:.1%}")
            print(f"   ✅ Hasil yang benar: {analisis['hasil_benar']}")
            if analisis['jenis_kesalahan']:
                print(f"   📝 Jenis kesalahan: {', '.join(analisis['jenis_kesalahan'])}")
        else:
            print(f"   ✅ KONVERSI BENAR")
        
        demo_dengan_jeda()

def demo_validasi_input():
    """Demo validasi input"""
    print("\n\n🎬 DEMO 5: VALIDASI INPUT")
    print("=" * 25)
    
    konverter = KonverterSistemBilangan()
    
    test_inputs = [
        ("101010", SistemBilangan.BINER, "Valid"),
        ("102010", SistemBilangan.BINER, "Invalid - digit 2"),
        ("ABC", SistemBilangan.HEKSADESIMAL, "Valid"),
        ("XYZ", SistemBilangan.HEKSADESIMAL, "Invalid - huruf X,Y,Z"),
        ("777", SistemBilangan.OKTAL, "Valid"),
        ("789", SistemBilangan.OKTAL, "Invalid - digit 8,9"),
    ]
    
    for nilai, sistem, expected in test_inputs:
        print(f"\n📍 Input: '{nilai}' untuk sistem {sistem.value}")
        demo_dengan_jeda(0.5)
        
        valid = konverter.validasi_input(nilai, sistem)
        status = "✅ VALID" if valid else "❌ INVALID"
        print(f"   Status: {status} ({expected})")

def main():
    """Menjalankan semua demo"""
    print("🚀 MEMULAI DEMONSTRASI SIMULATOR SISTEM BILANGAN")
    print("=" * 55)
    print("Program ini akan mendemonstrasikan semua fitur secara otomatis.")
    print("Tekan Ctrl+C kapan saja untuk menghentikan demo.")
    
    try:
        input("\n⏸️  Tekan Enter untuk memulai demo...")
        
        demo_konversi()
        demo_operasi_aritmatika()
        demo_simulasi_kesalahan()
        demo_deteksi_kesalahan()
        demo_validasi_input()
        
        print("\n\n🎉 DEMO SELESAI!")
        print("=" * 20)
        print("✨ Semua fitur telah didemonstrasikan.")
        print("🎮 Untuk pengalaman interaktif, jalankan: python number_system_simulator.py")
        
    except KeyboardInterrupt:
        print("\n\n🚪 Demo dihentikan oleh pengguna.")
        print("🎮 Untuk menjalankan program utama: python number_system_simulator.py")

if __name__ == "__main__":
    main()
