@echo off
echo 🔢 GUI Simulator Sistem Bilangan dengan Deteksi Kesalahan
echo ============================================================
echo.

REM Periksa apakah Python tersedia
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python tidak ditemukan. Pastikan Python terinstall dan ada di PATH.
    pause
    exit /b 1
)

echo ✅ Python tersedia
echo.

REM Tampilkan menu
echo Pilih mode:
echo 1. GUI Standar
echo 2. GUI dengan Demo
echo 3. Test Suite
echo 4. Bantuan
echo.

set /p choice="Masukkan pilihan (1-4): "

if "%choice%"=="1" (
    echo.
    echo 🖥️ Menjalankan GUI standar...
    python gui_simulator.py
) else if "%choice%"=="2" (
    echo.
    echo 🎬 Menjalankan GUI dengan demo...
    python demo_gui.py
) else if "%choice%"=="3" (
    echo.
    echo 🧪 Menjalankan test suite...
    python run_all_tests.py
) else if "%choice%"=="4" (
    echo.
    python start_gui.py --help-extended
) else (
    echo.
    echo ❌ Pilihan tidak valid.
    pause
    exit /b 1
)

echo.
echo ✅ Program selesai dijalankan.
pause
