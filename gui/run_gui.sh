#!/bin/bash

echo "🔢 GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan"
echo "============================================================"
echo

# Periksa apakah Python tersedia
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python tidak ditemukan. Pastikan Python terinstall."
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✅ Python tersedia: $($PYTHON_CMD --version)"

# Periksa file yang diperlukan
if [ ! -f "gui_simulator.py" ]; then
    echo "❌ File gui_simulator.py tidak ditemukan."
    exit 1
fi

if [ ! -f "number_system_simulator.py" ]; then
    echo "❌ File number_system_simulator.py tidak ditemukan."
    exit 1
fi

echo "✅ Semua file tersedia"
echo

# Tampilkan menu
echo "Pilih mode:"
echo "1. GUI Standar"
echo "2. GUI dengan Demo"
echo "3. Test Suite"
echo "4. Bantuan"
echo

read -p "Masukkan pilihan (1-4): " choice

case $choice in
    1)
        echo
        echo "🖥️ Menjalankan GUI standar..."
        $PYTHON_CMD gui_simulator.py
        ;;
    2)
        echo
        echo "🎬 Menjalankan GUI dengan demo..."
        $PYTHON_CMD demo_gui.py
        ;;
    3)
        echo
        echo "🧪 Menjalankan test suite..."
        $PYTHON_CMD test_simulator.py
        ;;
    4)
        echo
        $PYTHON_CMD run_gui.py --help-extended
        ;;
    *)
        echo
        echo "❌ Pilihan tidak valid."
        exit 1
        ;;
esac

echo
echo "✅ Program selesai dijalankan."
