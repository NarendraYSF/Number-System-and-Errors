#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite untuk GUI Simulator Sistem Bilangan
==============================================

Test ini memvalidasi semua fitur GUI dan memastikan tidak ada error.

Penulis: Kelompok 1
Tanggal: 5/9/2025
"""

import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
import sys
import os

# Tambahkan path untuk import module
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gui'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'main_logic'))

from gui_simulator import GUISimulatorSistemBilangan
from number_system_simulator import KonverterSistemBilangan, SistemBilangan, JenisKesalahan


class TestGUISimulator(unittest.TestCase):
    """Test class untuk GUI Simulator"""
    
    def setUp(self):
        """Setup untuk setiap test"""
        self.root = tk.Tk()
        self.root.withdraw()  # Sembunyikan window untuk test
        self.app = GUISimulatorSistemBilangan()
        
    def tearDown(self):
        """Cleanup setelah setiap test"""
        self.root.destroy()
        
    def test_gui_initialization(self):
        """Test inisialisasi GUI"""
        self.assertIsNotNone(self.app.root)
        self.assertIsNotNone(self.app.konverter)
        self.assertIsNotNone(self.app.notebook)
        
    def test_widget_creation(self):
        """Test pembuatan widget"""
        # Test notebook ada
        self.assertIsNotNone(self.app.notebook)
        
        # Test tab ada
        tabs = self.app.notebook.tabs()
        self.assertGreater(len(tabs), 0)
        
    def test_conversion_functionality(self):
        """Test fungsi konversi"""
        # Set test data
        self.app.from_system_var.set("desimal")
        self.app.input_value_var.set("42")
        self.app.to_system_var.set("biner")
        
        # Test konversi
        self.app.perform_conversion()
        
        # Verifikasi hasil ada di result_text
        result = self.app.result_text.get('1.0', tk.END)
        self.assertIn("101010", result)  # 42 dalam biner
        
    def test_arithmetic_functionality(self):
        """Test fungsi aritmatika"""
        # Set test data
        self.app.arithmetic_system_var.set("biner")
        self.app.value1_var.set("1010")
        self.app.value2_var.set("110")
        self.app.operation_var.set("+")
        
        # Test operasi
        self.app.perform_arithmetic()
        
        # Verifikasi hasil ada di arithmetic_result_text
        result = self.app.arithmetic_result_text.get('1.0', tk.END)
        self.assertIn("10000", result)  # 1010 + 110 = 10000
        
    def test_error_simulation_functionality(self):
        """Test fungsi simulasi kesalahan"""
        # Set test data
        self.app.error_system_var.set("biner")
        self.app.error_value_var.set("1010101")
        self.app.error_type_var.set("bit_flip")
        
        # Test simulasi
        self.app.simulate_error()
        
        # Verifikasi hasil ada di error_result_text
        result = self.app.error_result_text.get('1.0', tk.END)
        self.assertIn("1010101", result)  # Nilai asli
        
    def test_error_detection_functionality(self):
        """Test fungsi deteksi kesalahan"""
        # Set test data
        self.app.detect_from_system_var.set("desimal")
        self.app.detect_original_var.set("42")
        self.app.detect_to_system_var.set("biner")
        self.app.detect_result_var.set("101010")
        
        # Test deteksi
        self.app.detect_error()
        
        # Verifikasi hasil ada di detection_result_text
        result = self.app.detection_result_text.get('1.0', tk.END)
        self.assertIn("KONVERSI BENAR", result)  # 42 = 101010 (benar)
        
    def test_history_functionality(self):
        """Test fungsi riwayat"""
        # Test refresh history
        self.app.refresh_history()
        
        # Verifikasi history_text ada
        self.assertIsNotNone(self.app.history_text)
        
    def test_input_validation(self):
        """Test validasi input"""
        # Test input kosong
        self.app.input_value_var.set("")
        self.app.from_system_var.set("desimal")
        self.app.to_system_var.set("biner")
        
        # Test konversi dengan input kosong
        with patch('tkinter.messagebox.showwarning') as mock_warning:
            self.app.perform_conversion()
            mock_warning.assert_called_once()
            
    def test_invalid_input_handling(self):
        """Test penanganan input tidak valid"""
        # Test input tidak valid untuk biner
        self.app.input_value_var.set("123")  # Tidak valid untuk biner
        self.app.from_system_var.set("biner")
        self.app.to_system_var.set("desimal")
        
        # Test konversi dengan input tidak valid
        with patch('tkinter.messagebox.showerror') as mock_error:
            self.app.perform_conversion()
            mock_error.assert_called_once()
            
    def test_full_conversion_table(self):
        """Test tabel konversi lengkap"""
        # Set test data
        self.app.input_value_var.set("42")
        self.app.from_system_var.set("desimal")
        
        # Test tabel lengkap
        self.app.show_full_conversion_table()
        
        # Verifikasi hasil ada di result_text
        result = self.app.result_text.get('1.0', tk.END)
        self.assertIn("TABEL KONVERSI LENGKAP", result)
        
    def test_clear_history(self):
        """Test hapus riwayat"""
        # Tambahkan beberapa konversi ke riwayat
        self.app.konverter.riwayat_konversi.append({
            'nilai_asal': '42',
            'sistem_asal': 'desimal',
            'sistem_tujuan': 'biner',
            'hasil': '101010',
            'nilai_desimal': 42
        })
        
        # Test hapus riwayat
        with patch('tkinter.messagebox.askyesno', return_value=True):
            self.app.clear_history()
            
        # Verifikasi riwayat kosong
        self.assertEqual(len(self.app.konverter.riwayat_konversi), 0)


class TestGUIIntegration(unittest.TestCase):
    """Test integrasi GUI dengan engine konversi"""
    
    def setUp(self):
        """Setup untuk test integrasi"""
        self.konverter = KonverterSistemBilangan()
        
    def test_converter_integration(self):
        """Test integrasi dengan konverter"""
        # Test konversi dasar
        result = self.konverter.konversi("42", SistemBilangan.DESIMAL, SistemBilangan.BINER)
        self.assertEqual(result, "101010")
        
    def test_arithmetic_integration(self):
        """Test integrasi operasi aritmatika"""
        result = self.konverter.operasi_aritmatika("1010", "110", "+", SistemBilangan.BINER)
        self.assertTrue(result['berhasil'])
        self.assertEqual(result['hasil_sistem'], "10000")
        
    def test_error_simulation_integration(self):
        """Test integrasi simulasi kesalahan"""
        result_error, explanation = self.konverter.simulasi_kesalahan(
            "1010101", SistemBilangan.BINER, JenisKesalahan.BIT_FLIP
        )
        self.assertIsNotNone(result_error)
        self.assertIsNotNone(explanation)
        
    def test_error_detection_integration(self):
        """Test integrasi deteksi kesalahan"""
        analysis = self.konverter.deteksi_kesalahan_konversi(
            "42", "101010", SistemBilangan.DESIMAL, SistemBilangan.BINER
        )
        self.assertFalse(analysis['ada_kesalahan'])  # Konversi benar


class TestGUIPerformance(unittest.TestCase):
    """Test performa GUI"""
    
    def setUp(self):
        """Setup untuk test performa"""
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = GUISimulatorSistemBilangan()
        
    def tearDown(self):
        """Cleanup"""
        self.root.destroy()
        
    def test_gui_startup_time(self):
        """Test waktu startup GUI"""
        import time
        
        start_time = time.time()
        app = GUISimulatorSistemBilangan()
        end_time = time.time()
        
        startup_time = end_time - start_time
        self.assertLess(startup_time, 5.0)  # Harus kurang dari 5 detik
        
    def test_memory_usage(self):
        """Test penggunaan memori"""
        # Test sederhana tanpa psutil
        # Lakukan beberapa operasi dan pastikan tidak ada error
        for i in range(100):
            result = self.app.konverter.konversi(str(i), SistemBilangan.DESIMAL, SistemBilangan.BINER)
            self.assertIsNotNone(result)
            
        # Test bahwa riwayat tidak terlalu banyak
        self.assertLess(len(self.app.konverter.riwayat_konversi), 1000)


def run_gui_tests():
    """Menjalankan semua test GUI"""
    print("🧪 Menjalankan Test Suite untuk GUI Simulator Sistem Bilangan...")
    print("=" * 70)
    
    # Test suite
    test_suite = unittest.TestSuite()
    
    # Tambahkan test classes
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGUISimulator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGUIIntegration))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGUIPerformance))
    
    # Jalankan test
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Tampilkan hasil
    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("✅ Semua test berhasil!")
        print(f"📊 Total test: {result.testsRun}")
        print(f"⏱️ Waktu: {result.testsRun} test selesai")
    else:
        print("❌ Beberapa test gagal!")
        print(f"📊 Total test: {result.testsRun}")
        print(f"❌ Gagal: {len(result.failures)}")
        print(f"💥 Error: {len(result.errors)}")
        
        if result.failures:
            print("\n🔍 Test yang gagal:")
            for test, traceback in result.failures:
                print(f"  - {test}: {traceback}")
                
        if result.errors:
            print("\n💥 Test dengan error:")
            for test, traceback in result.errors:
                print(f"  - {test}: {traceback}")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_gui_tests()
    sys.exit(0 if success else 1)
