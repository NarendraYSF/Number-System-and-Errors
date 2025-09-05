#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo GUI Simulator Sistem Bilangan
==================================

Script ini mendemonstrasikan cara menggunakan GUI Simulator Sistem Bilangan
dengan contoh-contoh interaktif.

Penulis: AI Assistant
Tanggal: 2024
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from gui_simulator import GUISimulatorSistemBilangan
from main_logic import KonverterSistemBilangan, SistemBilangan, JenisKesalahan


class DemoGUISimulator(GUISimulatorSistemBilangan):
    """Kelas demo yang menambahkan fitur demonstrasi otomatis"""
    
    def __init__(self):
        super().__init__()
        self.add_demo_features()
        
    def add_demo_features(self):
        """Menambahkan fitur demo ke GUI"""
        # Tambahkan menu demo
        demo_frame = ttk.Frame(self.root)
        demo_frame.grid(row=0, column=0, sticky='ew', padx=10, pady=5)
        
        ttk.Button(demo_frame, text="🎬 Demo Otomatis", command=self.run_auto_demo).pack(side='left', padx=(0, 10))
        ttk.Button(demo_frame, text="📝 Contoh Konversi", command=self.demo_conversion).pack(side='left', padx=(0, 10))
        ttk.Button(demo_frame, text="🧮 Contoh Aritmatika", command=self.demo_arithmetic).pack(side='left', padx=(0, 10))
        ttk.Button(demo_frame, text="⚠️ Contoh Simulasi", command=self.demo_error_simulation).pack(side='left')
        
    def run_auto_demo(self):
        """Menjalankan demo otomatis"""
        demo_text = """
🎬 DEMO OTOMATIS SIMULATOR SISTEM BILANGAN

1️⃣ DEMO KONVERSI DASAR:
   Nilai: 42 (desimal)
   → Biner: 101010
   → Oktal: 52
   → Heksadesimal: 2A

2️⃣ DEMO OPERASI ARITMATIKA:
   Biner: 1010 + 110 = 10000 (16 desimal)
   Heksadesimal: FF + 1 = 100 (256 desimal)

3️⃣ DEMO SIMULASI KESALAHAN:
   Bit Flip: 1010101 → 1010001
   Salah Konversi: 1010101 → 10101010
   Overflow: 42 → 425

4️⃣ DEMO DETEKSI KESALAHAN:
   Input: 42 (desimal) → 101010 (biner) ✅ BENAR
   Input: 42 (desimal) → 101011 (biner) ❌ SALAH

🎓 Semua fitur ini dapat Anda coba langsung di tab-tab yang tersedia!
        """
        
        # Tampilkan di tab konversi
        self.notebook.select(0)  # Pilih tab konversi
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert('1.0', demo_text)
        
        messagebox.showinfo("Demo Otomatis", "Demo telah dimuat di tab Konversi!\nCoba fitur-fitur lainnya di tab yang berbeda.")
        
    def demo_conversion(self):
        """Demo konversi dengan contoh"""
        # Set contoh data
        self.from_system_var.set("desimal")
        self.input_value_var.set("42")
        self.to_system_var.set("biner")
        
        # Lakukan konversi otomatis
        self.perform_conversion()
        
        # Tampilkan tabel lengkap
        self.show_full_conversion_table()
        
        messagebox.showinfo("Demo Konversi", "Contoh konversi telah dimuat!\nCoba ubah nilai dan sistem untuk eksperimen lebih lanjut.")
        
    def demo_arithmetic(self):
        """Demo operasi aritmatika"""
        # Pindah ke tab aritmatika
        self.notebook.select(1)
        
        # Set contoh data
        self.arithmetic_system_var.set("biner")
        self.value1_var.set("1010")
        self.value2_var.set("110")
        self.operation_var.set("+")
        
        # Lakukan operasi
        self.perform_arithmetic()
        
        messagebox.showinfo("Demo Aritmatika", "Contoh operasi aritmatika telah dimuat!\nCoba operasi lain seperti *, /, %, **")
        
    def demo_error_simulation(self):
        """Demo simulasi kesalahan"""
        # Pindah ke tab simulasi kesalahan
        self.notebook.select(2)
        
        # Set contoh data
        self.error_system_var.set("biner")
        self.error_value_var.set("1010101")
        self.error_type_var.set("bit_flip")
        
        # Simulasikan kesalahan
        self.simulate_error()
        
        messagebox.showinfo("Demo Simulasi Kesalahan", "Contoh simulasi kesalahan telah dimuat!\nCoba jenis kesalahan lainnya untuk melihat perbedaannya.")


def main():
    """Fungsi main untuk menjalankan demo GUI"""
    try:
        print("🚀 Memulai Demo GUI Simulator Sistem Bilangan...")
        print("📋 Fitur yang tersedia:")
        print("   • Konversi antar sistem bilangan")
        print("   • Operasi aritmatika")
        print("   • Simulasi kesalahan")
        print("   • Deteksi kesalahan")
        print("   • Riwayat konversi")
        print("   • Bantuan lengkap")
        print("\n🎮 GUI akan terbuka dalam beberapa detik...")
        
        app = DemoGUISimulator()
        app.run()
        
    except Exception as e:
        print(f"❌ Error menjalankan demo GUI: {e}")
        print("💡 Pastikan semua file tersedia dan tkinter terinstall")


if __name__ == "__main__":
    main()
