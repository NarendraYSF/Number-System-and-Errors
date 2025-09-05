#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan
======================================================

Program ini menyediakan antarmuka grafis untuk Simulator Sistem Bilangan
dengan kemampuan konversi antar sistem dan simulasi kesalahan.

Fitur GUI:
- Konversi antar sistem bilangan dengan input/output visual
- Operasi aritmatika dalam berbagai sistem
- Simulasi dan deteksi kesalahan
- Riwayat konversi
- Interface yang user-friendly

Penulis: Kelompok 1
Tanggal: 5/9/2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter.font import Font
import threading
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from main_logic import KonverterSistemBilangan, SistemBilangan, JenisKesalahan


class GUISimulatorSistemBilangan:
    """Kelas utama untuk GUI Simulator Sistem Bilangan"""
    
    def __init__(self):
        """Inisialisasi GUI"""
        self.konverter = KonverterSistemBilangan()
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
        self.setup_styles()
        
    def setup_window(self):
        """Mengatur window utama"""
        self.root.title("🔢 Simulator Sistem Bilangan dengan Deteksi Kesalahan")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Icon dan konfigurasi
        try:
            self.root.iconbitmap("icon.ico")  # Jika ada file icon
        except:
            pass
            
        # Konfigurasi grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def setup_styles(self):
        """Mengatur style untuk GUI"""
        style = ttk.Style()
        
        # Konfigurasi tema
        style.theme_use('clam')
        
        # Style untuk notebook
        style.configure('TNotebook.Tab', padding=[12, 8])
        
        # Style untuk frame
        style.configure('Title.TFrame', background='#f0f0f0')
        style.configure('Content.TFrame', background='white')
        
        # Style untuk label
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        style.configure('Subtitle.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Info.TLabel', font=('Arial', 10), foreground='#666666')
        
    def create_widgets(self):
        """Membuat semua widget GUI"""
        # Frame utama
        main_frame = ttk.Frame(self.root, style='Content.TFrame')
        main_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Header
        self.create_header(main_frame)
        
        # Notebook untuk tab
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, sticky='nsew', pady=(10, 0))
        
        # Membuat tab-tab
        self.create_conversion_tab()
        self.create_arithmetic_tab()
        self.create_error_simulation_tab()
        self.create_error_detection_tab()
        self.create_history_tab()
        self.create_help_tab()
        
    def create_header(self, parent):
        """Membuat header aplikasi"""
        header_frame = ttk.Frame(parent, style='Title.TFrame')
        header_frame.grid(row=0, column=0, sticky='ew', pady=(0, 10))
        header_frame.grid_columnconfigure(0, weight=1)
        
        title_label = ttk.Label(
            header_frame, 
            text="🔢 Simulator Sistem Bilangan dengan Deteksi Kesalahan",
            style='Title.TLabel'
        )
        title_label.grid(row=0, column=0, pady=10)
        
        subtitle_label = ttk.Label(
            header_frame,
            text="Konversi antar sistem bilangan, operasi aritmatika, dan simulasi kesalahan",
            style='Info.TLabel'
        )
        subtitle_label.grid(row=1, column=0, pady=(0, 10))
        
    def create_conversion_tab(self):
        """Membuat tab konversi antar sistem bilangan"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="🔄 Konversi")
        
        # Frame utama
        main_frame = ttk.Frame(tab_frame)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding=10)
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Sistem asal
        ttk.Label(input_frame, text="Sistem Asal:", style='Subtitle.TLabel').grid(row=0, column=0, sticky='w', pady=5)
        self.from_system_var = tk.StringVar(value="desimal")
        from_combo = ttk.Combobox(input_frame, textvariable=self.from_system_var, 
                                 values=["biner", "desimal", "oktal", "heksadesimal"],
                                 state="readonly", width=15)
        from_combo.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Nilai input
        ttk.Label(input_frame, text="Nilai:", style='Subtitle.TLabel').grid(row=1, column=0, sticky='w', pady=5)
        self.input_value_var = tk.StringVar()
        input_entry = ttk.Entry(input_frame, textvariable=self.input_value_var, width=20)
        input_entry.grid(row=1, column=1, sticky='w', padx=(10, 0), pady=5)
        input_entry.bind('<KeyRelease>', self.on_input_change)
        
        # Sistem tujuan
        ttk.Label(input_frame, text="Sistem Tujuan:", style='Subtitle.TLabel').grid(row=2, column=0, sticky='w', pady=5)
        self.to_system_var = tk.StringVar(value="biner")
        to_combo = ttk.Combobox(input_frame, textvariable=self.to_system_var,
                               values=["biner", "desimal", "oktal", "heksadesimal"],
                               state="readonly", width=15)
        to_combo.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Tombol konversi
        convert_btn = ttk.Button(input_frame, text="🔄 Konversi", command=self.perform_conversion)
        convert_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Output section
        output_frame = ttk.LabelFrame(main_frame, text="Hasil Konversi", padding=10)
        output_frame.pack(fill='both', expand=True)
        
        # Hasil konversi
        self.result_text = scrolledtext.ScrolledText(output_frame, height=8, width=60, wrap=tk.WORD)
        self.result_text.pack(fill='both', expand=True)
        
        # Tabel konversi lengkap
        ttk.Button(output_frame, text="📊 Tampilkan Tabel Lengkap", 
                  command=self.show_full_conversion_table).pack(pady=10)
        
    def create_arithmetic_tab(self):
        """Membuat tab operasi aritmatika"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="🧮 Aritmatika")
        
        main_frame = ttk.Frame(tab_frame)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Operasi Aritmatika", padding=10)
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Sistem bilangan
        ttk.Label(input_frame, text="Sistem Bilangan:", style='Subtitle.TLabel').grid(row=0, column=0, sticky='w', pady=5)
        self.arithmetic_system_var = tk.StringVar(value="desimal")
        system_combo = ttk.Combobox(input_frame, textvariable=self.arithmetic_system_var,
                                   values=["biner", "desimal", "oktal", "heksadesimal"],
                                   state="readonly", width=15)
        system_combo.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Nilai pertama
        ttk.Label(input_frame, text="Nilai Pertama:", style='Subtitle.TLabel').grid(row=1, column=0, sticky='w', pady=5)
        self.value1_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.value1_var, width=20).grid(row=1, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Operasi
        ttk.Label(input_frame, text="Operasi:", style='Subtitle.TLabel').grid(row=2, column=0, sticky='w', pady=5)
        self.operation_var = tk.StringVar(value="+")
        op_combo = ttk.Combobox(input_frame, textvariable=self.operation_var,
                               values=["+", "-", "*", "/", "%", "**"],
                               state="readonly", width=15)
        op_combo.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Nilai kedua
        ttk.Label(input_frame, text="Nilai Kedua:", style='Subtitle.TLabel').grid(row=3, column=0, sticky='w', pady=5)
        self.value2_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.value2_var, width=20).grid(row=3, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Tombol hitung
        ttk.Button(input_frame, text="🧮 Hitung", command=self.perform_arithmetic).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Output section
        output_frame = ttk.LabelFrame(main_frame, text="Hasil Operasi", padding=10)
        output_frame.pack(fill='both', expand=True)
        
        self.arithmetic_result_text = scrolledtext.ScrolledText(output_frame, height=8, width=60, wrap=tk.WORD)
        self.arithmetic_result_text.pack(fill='both', expand=True)
        
    def create_error_simulation_tab(self):
        """Membuat tab simulasi kesalahan"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="⚠️ Simulasi Kesalahan")
        
        main_frame = ttk.Frame(tab_frame)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Simulasi Kesalahan", padding=10)
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Sistem bilangan
        ttk.Label(input_frame, text="Sistem Bilangan:", style='Subtitle.TLabel').grid(row=0, column=0, sticky='w', pady=5)
        self.error_system_var = tk.StringVar(value="biner")
        system_combo = ttk.Combobox(input_frame, textvariable=self.error_system_var,
                                   values=["biner", "desimal", "oktal", "heksadesimal"],
                                   state="readonly", width=15)
        system_combo.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Nilai input
        ttk.Label(input_frame, text="Nilai:", style='Subtitle.TLabel').grid(row=1, column=0, sticky='w', pady=5)
        self.error_value_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.error_value_var, width=20).grid(row=1, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Jenis kesalahan
        ttk.Label(input_frame, text="Jenis Kesalahan:", style='Subtitle.TLabel').grid(row=2, column=0, sticky='w', pady=5)
        self.error_type_var = tk.StringVar(value="bit_flip")
        error_combo = ttk.Combobox(input_frame, textvariable=self.error_type_var,
                                  values=["bit_flip", "salah_konversi", "salah_interpretasi", "overflow", "underflow"],
                                  state="readonly", width=15)
        error_combo.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Tombol simulasi
        ttk.Button(input_frame, text="⚠️ Simulasikan Kesalahan", command=self.simulate_error).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Output section
        output_frame = ttk.LabelFrame(main_frame, text="Hasil Simulasi", padding=10)
        output_frame.pack(fill='both', expand=True)
        
        self.error_result_text = scrolledtext.ScrolledText(output_frame, height=8, width=60, wrap=tk.WORD)
        self.error_result_text.pack(fill='both', expand=True)
        
    def create_error_detection_tab(self):
        """Membuat tab deteksi kesalahan"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="🔍 Deteksi Kesalahan")
        
        main_frame = ttk.Frame(tab_frame)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Deteksi Kesalahan Konversi", padding=10)
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Sistem asal
        ttk.Label(input_frame, text="Sistem Asal:", style='Subtitle.TLabel').grid(row=0, column=0, sticky='w', pady=5)
        self.detect_from_system_var = tk.StringVar(value="desimal")
        from_combo = ttk.Combobox(input_frame, textvariable=self.detect_from_system_var,
                                 values=["biner", "desimal", "oktal", "heksadesimal"],
                                 state="readonly", width=15)
        from_combo.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Nilai asal
        ttk.Label(input_frame, text="Nilai Asal:", style='Subtitle.TLabel').grid(row=1, column=0, sticky='w', pady=5)
        self.detect_original_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.detect_original_var, width=20).grid(row=1, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Sistem tujuan
        ttk.Label(input_frame, text="Sistem Tujuan:", style='Subtitle.TLabel').grid(row=2, column=0, sticky='w', pady=5)
        self.detect_to_system_var = tk.StringVar(value="biner")
        to_combo = ttk.Combobox(input_frame, textvariable=self.detect_to_system_var,
                               values=["biner", "desimal", "oktal", "heksadesimal"],
                               state="readonly", width=15)
        to_combo.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Hasil yang akan diperiksa
        ttk.Label(input_frame, text="Hasil yang Diperiksa:", style='Subtitle.TLabel').grid(row=3, column=0, sticky='w', pady=5)
        self.detect_result_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.detect_result_var, width=20).grid(row=3, column=1, sticky='w', padx=(10, 0), pady=5)
        
        # Tombol deteksi
        ttk.Button(input_frame, text="🔍 Deteksi Kesalahan", command=self.detect_error).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Output section
        output_frame = ttk.LabelFrame(main_frame, text="Hasil Deteksi", padding=10)
        output_frame.pack(fill='both', expand=True)
        
        self.detection_result_text = scrolledtext.ScrolledText(output_frame, height=8, width=60, wrap=tk.WORD)
        self.detection_result_text.pack(fill='both', expand=True)
        
    def create_history_tab(self):
        """Membuat tab riwayat konversi"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="📜 Riwayat")
        
        main_frame = ttk.Frame(tab_frame)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Control frame
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Button(control_frame, text="🔄 Refresh", command=self.refresh_history).pack(side='left', padx=(0, 10))
        ttk.Button(control_frame, text="🗑️ Hapus Riwayat", command=self.clear_history).pack(side='left')
        
        # History display
        history_frame = ttk.LabelFrame(main_frame, text="Riwayat Konversi", padding=10)
        history_frame.pack(fill='both', expand=True)
        
        self.history_text = scrolledtext.ScrolledText(history_frame, height=15, width=70, wrap=tk.WORD)
        self.history_text.pack(fill='both', expand=True)
        
        # Load initial history
        self.refresh_history()
        
    def create_help_tab(self):
        """Membuat tab bantuan"""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="❓ Bantuan")
        
        main_frame = ttk.Frame(tab_frame)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        help_text = scrolledtext.ScrolledText(main_frame, height=20, width=70, wrap=tk.WORD)
        help_text.pack(fill='both', expand=True)
        
        # Content bantuan
        help_content = """
🔢 SIMULATOR SISTEM BILANGAN DENGAN DETEKSI KESALAHAN

📚 SISTEM BILANGAN YANG DIDUKUNG:
• Biner (Base-2): Menggunakan digit 0, 1
• Desimal (Base-10): Menggunakan digit 0-9  
• Oktal (Base-8): Menggunakan digit 0-7
• Heksadesimal (Base-16): Menggunakan digit 0-9, A-F

🔧 FITUR PROGRAM:
• Konversi akurat antar semua sistem bilangan
• Operasi aritmatika dalam sistem bilangan apapun
• Simulasi berbagai jenis kesalahan
• Deteksi kesalahan dalam hasil konversi
• Validasi input yang ketat
• Riwayat konversi

⚠️ JENIS KESALAHAN YANG DAPAT DISIMULASIKAN:
• Bit Flip: Perubahan bit acak (0→1 atau 1→0)
• Salah Konversi: Kesalahan dalam proses konversi
• Salah Interpretasi: Salah mengidentifikasi sistem bilangan
• Overflow: Nilai melebihi kapasitas
• Underflow: Nilai kurang dari minimum

💡 CARA PENGGUNAAN:

1. TAB KONVERSI:
   - Pilih sistem asal dan tujuan
   - Masukkan nilai yang akan dikonversi
   - Klik tombol "Konversi"
   - Lihat hasil di area output

2. TAB ARITMATIKA:
   - Pilih sistem bilangan
   - Masukkan dua nilai dan operasi
   - Klik tombol "Hitung"
   - Lihat hasil operasi

3. TAB SIMULASI KESALAHAN:
   - Pilih sistem bilangan dan jenis kesalahan
   - Masukkan nilai
   - Klik tombol "Simulasikan Kesalahan"
   - Lihat bagaimana kesalahan mempengaruhi hasil

4. TAB DETEKSI KESALAHAN:
   - Masukkan nilai asal dan hasil konversi
   - Pilih sistem asal dan tujuan
   - Klik tombol "Deteksi Kesalahan"
   - Lihat analisis kesalahan

5. TAB RIWAYAT:
   - Lihat semua konversi yang telah dilakukan
   - Refresh atau hapus riwayat

💡 TIPS PENGGUNAAN:
• Gunakan huruf kapital untuk heksadesimal (A-F)
• Program hanya mendukung bilangan positif
• Semua operasi dilakukan secara real-time
• Riwayat disimpan otomatis

🎓 Semoga program ini membantu Anda memahami sistem bilangan dengan lebih baik!
        """
        
        help_text.insert('1.0', help_content)
        help_text.config(state='disabled')
        
    def on_input_change(self, event=None):
        """Event handler untuk perubahan input"""
        # Validasi input real-time bisa ditambahkan di sini
        pass
        
    def perform_conversion(self):
        """Melakukan konversi antar sistem bilangan"""
        try:
            # Ambil input
            input_value = self.input_value_var.get().strip()
            from_system = self.from_system_var.get()
            to_system = self.to_system_var.get()
            
            if not input_value:
                messagebox.showwarning("Peringatan", "Masukkan nilai yang akan dikonversi!")
                return
                
            # Validasi input
            from_system_enum = SistemBilangan(from_system)
            if not self.konverter.validasi_input(input_value, from_system_enum):
                messagebox.showerror("Error", f"Input '{input_value}' tidak valid untuk sistem {from_system}!")
                return
                
            # Lakukan konversi
            to_system_enum = SistemBilangan(to_system)
            result = self.konverter.konversi(input_value, from_system_enum, to_system_enum)
            
            # Tampilkan hasil
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert('1.0', f"🔄 HASIL KONVERSI:\n")
            self.result_text.insert(tk.END, f"   {from_system.capitalize()}: {input_value}\n")
            self.result_text.insert(tk.END, f"   {to_system.capitalize()}: {result}\n")
            
            # Tampilkan nilai desimal sebagai referensi
            decimal_value = self.konverter.ke_desimal(input_value, from_system_enum)
            self.result_text.insert(tk.END, f"   Nilai desimal: {decimal_value}\n")
            
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            
    def show_full_conversion_table(self):
        """Menampilkan tabel konversi lengkap"""
        try:
            input_value = self.input_value_var.get().strip()
            from_system = self.from_system_var.get()
            
            if not input_value:
                messagebox.showwarning("Peringatan", "Masukkan nilai terlebih dahulu!")
                return
                
            from_system_enum = SistemBilangan(from_system)
            if not self.konverter.validasi_input(input_value, from_system_enum):
                messagebox.showerror("Error", f"Input '{input_value}' tidak valid untuk sistem {from_system}!")
                return
                
            # Buat tabel konversi lengkap
            table = self.konverter.tampilkan_tabel_konversi(input_value, from_system_enum)
            
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert('1.0', f"📊 TABEL KONVERSI LENGKAP untuk '{input_value}' ({from_system}):\n")
            self.result_text.insert(tk.END, "=" * 50 + "\n")
            
            for system, result in table.items():
                if system != 'error':
                    self.result_text.insert(tk.END, f"   {system.capitalize():<12}: {result}\n")
                    
            if 'error' in table:
                self.result_text.insert(tk.END, f"\n❌ Error: {table['error']}\n")
                
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            
    def perform_arithmetic(self):
        """Melakukan operasi aritmatika"""
        try:
            # Ambil input
            value1 = self.value1_var.get().strip()
            value2 = self.value2_var.get().strip()
            operation = self.operation_var.get()
            system = self.arithmetic_system_var.get()
            
            if not value1 or not value2:
                messagebox.showwarning("Peringatan", "Masukkan kedua nilai!")
                return
                
            # Validasi input
            system_enum = SistemBilangan(system)
            if not self.konverter.validasi_input(value1, system_enum):
                messagebox.showerror("Error", f"Nilai pertama '{value1}' tidak valid untuk sistem {system}!")
                return
            if not self.konverter.validasi_input(value2, system_enum):
                messagebox.showerror("Error", f"Nilai kedua '{value2}' tidak valid untuk sistem {system}!")
                return
                
            # Lakukan operasi
            result = self.konverter.operasi_aritmatika(value1, value2, operation, system_enum)
            
            # Tampilkan hasil
            self.arithmetic_result_text.delete('1.0', tk.END)
            
            if result['berhasil']:
                self.arithmetic_result_text.insert('1.0', f"🧮 HASIL OPERASI ARITMATIKA:\n")
                self.arithmetic_result_text.insert(tk.END, f"   Operasi: {result['operasi']}\n")
                self.arithmetic_result_text.insert(tk.END, f"   Sistem: {result['sistem']}\n")
                self.arithmetic_result_text.insert(tk.END, f"   Hasil ({system}): {result['hasil_sistem']}\n")
                self.arithmetic_result_text.insert(tk.END, f"   Hasil (desimal): {result['hasil_desimal']}\n")
            else:
                self.arithmetic_result_text.insert('1.0', f"❌ ERROR:\n")
                self.arithmetic_result_text.insert(tk.END, f"   {result['error']}\n")
                
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            
    def simulate_error(self):
        """Mensimulasikan kesalahan"""
        try:
            # Ambil input
            value = self.error_value_var.get().strip()
            system = self.error_system_var.get()
            error_type = self.error_type_var.get()
            
            if not value:
                messagebox.showwarning("Peringatan", "Masukkan nilai!")
                return
                
            # Validasi input
            system_enum = SistemBilangan(system)
            if not self.konverter.validasi_input(value, system_enum):
                messagebox.showerror("Error", f"Input '{value}' tidak valid untuk sistem {system}!")
                return
                
            # Konversi jenis kesalahan
            error_type_enum = JenisKesalahan(error_type)
            
            # Simulasikan kesalahan
            result_error, explanation = self.konverter.simulasi_kesalahan(value, system_enum, error_type_enum)
            
            # Tampilkan hasil
            self.error_result_text.delete('1.0', tk.END)
            self.error_result_text.insert('1.0', f"⚠️ HASIL SIMULASI KESALAHAN:\n")
            self.error_result_text.insert(tk.END, f"   Nilai asli: {value}\n")
            self.error_result_text.insert(tk.END, f"   Nilai dengan kesalahan: {result_error}\n")
            self.error_result_text.insert(tk.END, f"   Penjelasan: {explanation}\n")
            
            # Tampilkan dampak kesalahan jika berbeda
            if result_error != value:
                try:
                    original_decimal = self.konverter.ke_desimal(value, system_enum)
                    if self.konverter.validasi_input(result_error, system_enum):
                        error_decimal = self.konverter.ke_desimal(result_error, system_enum)
                        difference = abs(error_decimal - original_decimal)
                        self.error_result_text.insert(tk.END, f"   Dampak kesalahan: Selisih {difference} dalam desimal\n")
                    else:
                        self.error_result_text.insert(tk.END, f"   Dampak kesalahan: Hasil tidak valid untuk sistem {system}\n")
                except:
                    self.error_result_text.insert(tk.END, f"   Dampak kesalahan: Tidak dapat dihitung\n")
                    
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            
    def detect_error(self):
        """Mendeteksi kesalahan dalam konversi"""
        try:
            # Ambil input
            original_value = self.detect_original_var.get().strip()
            result_value = self.detect_result_var.get().strip()
            from_system = self.detect_from_system_var.get()
            to_system = self.detect_to_system_var.get()
            
            if not original_value or not result_value:
                messagebox.showwarning("Peringatan", "Masukkan nilai asal dan hasil yang akan diperiksa!")
                return
                
            # Validasi input
            from_system_enum = SistemBilangan(from_system)
            if not self.konverter.validasi_input(original_value, from_system_enum):
                messagebox.showerror("Error", f"Nilai asal '{original_value}' tidak valid untuk sistem {from_system}!")
                return
                
            to_system_enum = SistemBilangan(to_system)
            if not self.konverter.validasi_input(result_value, to_system_enum):
                messagebox.showerror("Error", f"Hasil '{result_value}' tidak valid untuk sistem {to_system}!")
                return
                
            # Lakukan deteksi kesalahan
            analysis = self.konverter.deteksi_kesalahan_konversi(
                original_value, result_value, from_system_enum, to_system_enum
            )
            
            # Tampilkan hasil
            self.detection_result_text.delete('1.0', tk.END)
            self.detection_result_text.insert('1.0', f"🔍 HASIL ANALISIS KESALAHAN:\n")
            self.detection_result_text.insert(tk.END, f"   Nilai asal ({from_system}): {original_value}\n")
            self.detection_result_text.insert(tk.END, f"   Hasil input ({to_system}): {result_value}\n")
            self.detection_result_text.insert(tk.END, f"   Hasil yang benar: {analysis['hasil_benar']}\n")
            
            if analysis['ada_kesalahan']:
                self.detection_result_text.insert(tk.END, f"   ❌ Status: KESALAHAN TERDETEKSI\n")
                self.detection_result_text.insert(tk.END, f"   🎯 Tingkat kepercayaan: {analysis['tingkat_kepercayaan']:.1%}\n")
                if analysis['jenis_kesalahan']:
                    self.detection_result_text.insert(tk.END, f"   📝 Jenis kesalahan:\n")
                    for error in analysis['jenis_kesalahan']:
                        self.detection_result_text.insert(tk.END, f"      • {error}\n")
            else:
                self.detection_result_text.insert(tk.END, f"   ✅ Status: KONVERSI BENAR\n")
                
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            
    def refresh_history(self):
        """Refresh riwayat konversi"""
        self.history_text.delete('1.0', tk.END)
        
        if not self.konverter.riwayat_konversi:
            self.history_text.insert('1.0', "📭 Belum ada riwayat konversi.")
            return
            
        self.history_text.insert('1.0', f"📜 RIWAYAT KONVERSI (Total: {len(self.konverter.riwayat_konversi)})\n")
        self.history_text.insert(tk.END, "=" * 60 + "\n")
        
        for i, entry in enumerate(self.konverter.riwayat_konversi[-20:], 1):  # Tampilkan 20 terakhir
            self.history_text.insert(tk.END, f"{i:2d}. {entry['nilai_asal']} ({entry['sistem_asal']}) → "
                                          f"{entry['hasil']} ({entry['sistem_tujuan']}) "
                                          f"[desimal: {entry['nilai_desimal']}]\n")
            
    def clear_history(self):
        """Hapus riwayat konversi"""
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus semua riwayat konversi?"):
            self.konverter.riwayat_konversi.clear()
            self.refresh_history()
            
    def run(self):
        """Menjalankan aplikasi GUI"""
        self.root.mainloop()


def main():
    """Fungsi main untuk menjalankan GUI"""
    try:
        app = GUISimulatorSistemBilangan()
        app.run()
    except Exception as e:
        print(f"Error menjalankan aplikasi: {e}")


if __name__ == "__main__":
    main()
