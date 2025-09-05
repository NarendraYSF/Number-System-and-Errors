#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konfigurasi untuk GUI Simulator Sistem Bilangan
===============================================

File ini berisi konfigurasi untuk GUI, termasuk tema, warna, dan pengaturan lainnya.

Penulis: AI Assistant
Tanggal: 2024
"""

# Konfigurasi Tema dan Warna - Modern Minimalis
THEME_CONFIG = {
    # Light Theme
    'light': {
        'primary_color': '#2563EB',      # Blue 600 - Modern blue
        'primary_hover': '#1D4ED8',      # Blue 700 - Hover state
        'secondary_color': '#7C3AED',    # Violet 600 - Modern purple
        'success_color': '#059669',      # Emerald 600 - Modern green
        'warning_color': '#DC2626',      # Red 600 - Modern red
        'background_color': '#FFFFFF',   # Pure white
        'surface_color': '#F8FAFC',      # Slate 50 - Card background
        'text_primary': '#0F172A',       # Slate 900 - Primary text
        'text_secondary': '#475569',     # Slate 600 - Secondary text
        'text_muted': '#94A3B8',         # Slate 400 - Muted text
        'border_color': '#E2E8F0',       # Slate 200 - Border
        'border_focus': '#2563EB',       # Blue 600 - Focus border
        'shadow_color': '#00000010',     # Subtle shadow
    },
    # Dark Theme
    'dark': {
        'primary_color': '#3B82F6',      # Blue 500 - Lighter for dark mode
        'primary_hover': '#2563EB',      # Blue 600 - Hover state
        'secondary_color': '#8B5CF6',    # Violet 500 - Lighter for dark mode
        'success_color': '#10B981',      # Emerald 500 - Lighter for dark mode
        'warning_color': '#EF4444',      # Red 500 - Lighter for dark mode
        'background_color': '#0F172A',   # Slate 900 - Dark background
        'surface_color': '#1E293B',      # Slate 800 - Card background
        'text_primary': '#F8FAFC',       # Slate 50 - Primary text
        'text_secondary': '#CBD5E1',     # Slate 300 - Secondary text
        'text_muted': '#64748B',         # Slate 500 - Muted text
        'border_color': '#334155',       # Slate 700 - Border
        'border_focus': '#3B82F6',       # Blue 500 - Focus border
        'shadow_color': '#00000040',     # Darker shadow
    }
}

# Konfigurasi Font - Modern Typography
FONT_CONFIG = {
    'title_font': ('Segoe UI', 20, 'bold'),           # Modern system font
    'subtitle_font': ('Segoe UI', 14, 'bold'),        # Clean subtitle (semibold not supported)
    'body_font': ('Segoe UI', 11),                    # Readable body text
    'monospace_font': ('Consolas', 10),               # Modern monospace
    'small_font': ('Segoe UI', 9),                    # Small text
    'button_font': ('Segoe UI', 10, 'bold'),          # Button text (medium not supported)
    'label_font': ('Segoe UI', 10, 'bold'),           # Label text (medium not supported)
}

# Konfigurasi Window
WINDOW_CONFIG = {
    'title': '🔢 Simulator Sistem Bilangan dengan Deteksi Kesalahan',
    'min_width': 800,
    'min_height': 600,
    'default_width': 900,
    'default_height': 700,
    'resizable': True,
}

# Konfigurasi Tab - Minimalis
TAB_CONFIG = {
    'conversion': {
        'title': 'Konversi',
        'description': 'Konversi antar sistem bilangan',
        'icon': '↔'
    },
    'arithmetic': {
        'title': 'Aritmatika',
        'description': 'Operasi aritmatika dalam berbagai sistem',
        'icon': '±'
    },
    'error_simulation': {
        'title': 'Simulasi',
        'description': 'Simulasi berbagai jenis kesalahan',
        'icon': '⚠'
    },
    'error_detection': {
        'title': 'Deteksi',
        'description': 'Deteksi kesalahan dalam konversi',
        'icon': '🔍'
    },
    'history': {
        'title': 'Riwayat',
        'description': 'Riwayat konversi yang telah dilakukan',
        'icon': '📋'
    },
    'help': {
        'title': 'Bantuan',
        'description': 'Panduan dan informasi bantuan',
        'icon': '?'
    }
}

# Konfigurasi Sistem Bilangan
NUMBER_SYSTEM_CONFIG = {
    'biner': {
        'name': 'Biner',
        'base': 2,
        'digits': '01',
        'example': '101010',
        'description': 'Sistem bilangan basis 2'
    },
    'desimal': {
        'name': 'Desimal',
        'base': 10,
        'digits': '0123456789',
        'example': '42',
        'description': 'Sistem bilangan basis 10'
    },
    'oktal': {
        'name': 'Oktal',
        'base': 8,
        'digits': '01234567',
        'example': '52',
        'description': 'Sistem bilangan basis 8'
    },
    'heksadesimal': {
        'name': 'Heksadesimal',
        'base': 16,
        'digits': '0123456789ABCDEF',
        'example': '2A',
        'description': 'Sistem bilangan basis 16'
    }
}

# Konfigurasi Jenis Kesalahan
ERROR_TYPE_CONFIG = {
    'bit_flip': {
        'name': 'Bit Flip',
        'description': 'Perubahan bit acak (0→1 atau 1→0)',
        'icon': '🔀'
    },
    'salah_konversi': {
        'name': 'Salah Konversi',
        'description': 'Kesalahan dalam proses konversi',
        'icon': '🔄'
    },
    'salah_interpretasi': {
        'name': 'Salah Interpretasi',
        'description': 'Salah mengidentifikasi sistem bilangan',
        'icon': '🤔'
    },
    'overflow': {
        'name': 'Overflow',
        'description': 'Nilai melebihi kapasitas',
        'icon': '📈'
    },
    'underflow': {
        'name': 'Underflow',
        'description': 'Nilai kurang dari minimum',
        'icon': '📉'
    }
}

# Konfigurasi Operasi Aritmatika
ARITHMETIC_OPERATIONS = {
    '+': {
        'name': 'Penjumlahan',
        'symbol': '+',
        'description': 'Menambahkan dua nilai'
    },
    '-': {
        'name': 'Pengurangan',
        'symbol': '-',
        'description': 'Mengurangi nilai kedua dari nilai pertama'
    },
    '*': {
        'name': 'Perkalian',
        'symbol': '×',
        'description': 'Mengalikan dua nilai'
    },
    '/': {
        'name': 'Pembagian',
        'symbol': '÷',
        'description': 'Membagi nilai pertama dengan nilai kedua'
    },
    '%': {
        'name': 'Modulo',
        'symbol': '%',
        'description': 'Sisa pembagian nilai pertama dengan nilai kedua'
    },
    '**': {
        'name': 'Pangkat',
        'symbol': '^',
        'description': 'Nilai pertama dipangkatkan nilai kedua'
    }
}

# Konfigurasi Pesan
MESSAGE_CONFIG = {
    'success': {
        'conversion': '✅ Konversi berhasil!',
        'arithmetic': '✅ Operasi aritmatika berhasil!',
        'simulation': '✅ Simulasi kesalahan berhasil!',
        'detection': '✅ Deteksi kesalahan berhasil!'
    },
    'error': {
        'invalid_input': '❌ Input tidak valid!',
        'conversion_failed': '❌ Konversi gagal!',
        'arithmetic_failed': '❌ Operasi aritmatika gagal!',
        'simulation_failed': '❌ Simulasi kesalahan gagal!',
        'detection_failed': '❌ Deteksi kesalahan gagal!'
    },
    'warning': {
        'empty_input': '⚠️ Masukkan nilai terlebih dahulu!',
        'invalid_system': '⚠️ Sistem bilangan tidak valid!',
        'division_by_zero': '⚠️ Pembagian dengan nol tidak diperbolehkan!'
    },
    'info': {
        'demo_loaded': 'ℹ️ Demo telah dimuat!',
        'history_cleared': 'ℹ️ Riwayat telah dihapus!',
        'help_available': 'ℹ️ Bantuan tersedia di tab Bantuan!'
    }
}

# Konfigurasi Validasi
VALIDATION_CONFIG = {
    'max_input_length': 50,
    'max_history_entries': 100,
    'max_display_history': 20,
    'timeout_seconds': 30,
}

# Konfigurasi Demo
DEMO_CONFIG = {
    'examples': {
        'conversion': {
            'value': '42',
            'from_system': 'desimal',
            'to_system': 'biner'
        },
        'arithmetic': {
            'value1': '1010',
            'value2': '110',
            'operation': '+',
            'system': 'biner'
        },
        'error_simulation': {
            'value': '1010101',
            'system': 'biner',
            'error_type': 'bit_flip'
        },
        'error_detection': {
            'original': '42',
            'result': '101010',
            'from_system': 'desimal',
            'to_system': 'biner'
        }
    }
}

# Konfigurasi Layout - Modern Minimalis
LAYOUT_CONFIG = {
    'padding': 16,                    # Increased padding for breathing room
    'spacing': 8,                     # Consistent spacing
    'border_width': 1,                # Thin borders
    'corner_radius': 8,               # Modern rounded corners
    'tab_padding': (16, 12),          # Comfortable tab padding
    'button_padding': (12, 8),        # Button padding
    'card_padding': 20,               # Card internal padding
    'input_padding': 12,              # Input field padding
    'section_spacing': 24,            # Space between sections
    'element_spacing': 12,            # Space between elements
}

# Konfigurasi Performance
PERFORMANCE_CONFIG = {
    'max_concurrent_operations': 5,
    'cache_size': 1000,
    'auto_save_interval': 300,  # 5 menit
    'max_memory_usage': 100,    # MB
}

# Konfigurasi Dark Mode
DARK_MODE_CONFIG = {
    'enabled': False,  # Default to light mode
    'auto_detect': True,  # Auto detect system theme
    'toggle_hotkey': '<Control-d>',  # Hotkey for toggle
}

# Fungsi untuk mendapatkan konfigurasi
def get_config(section, key=None, theme='light'):
    """Mendapatkan konfigurasi berdasarkan section dan key"""
    configs = {
        'theme': THEME_CONFIG,
        'font': FONT_CONFIG,
        'window': WINDOW_CONFIG,
        'tab': TAB_CONFIG,
        'number_system': NUMBER_SYSTEM_CONFIG,
        'error_type': ERROR_TYPE_CONFIG,
        'arithmetic': ARITHMETIC_OPERATIONS,
        'message': MESSAGE_CONFIG,
        'validation': VALIDATION_CONFIG,
        'demo': DEMO_CONFIG,
        'layout': LAYOUT_CONFIG,
        'performance': PERFORMANCE_CONFIG,
        'dark_mode': DARK_MODE_CONFIG
    }
    
    if section not in configs:
        raise ValueError(f"Section '{section}' tidak ditemukan")
    
    if key is None:
        return configs[section]
    
    # Special handling for theme colors
    if section == 'theme' and key in THEME_CONFIG.get(theme, {}):
        return THEME_CONFIG[theme][key]
    elif section == 'theme' and key in THEME_CONFIG['light']:
        return THEME_CONFIG['light'][key]  # Fallback to light theme
    
    if key not in configs[section]:
        raise ValueError(f"Key '{key}' tidak ditemukan di section '{section}'")
    
    return configs[section][key]

def get_theme_colors(theme='light'):
    """Mendapatkan semua warna untuk tema tertentu"""
    return THEME_CONFIG.get(theme, THEME_CONFIG['light'])

# Fungsi untuk validasi konfigurasi
def validate_config():
    """Memvalidasi semua konfigurasi"""
    errors = []
    
    # Validasi tema - check both light and dark themes
    required_colors = ['primary_color', 'secondary_color', 'background_color', 'text_primary']
    for theme in ['light', 'dark']:
        if theme in THEME_CONFIG:
            for color in required_colors:
                if color not in THEME_CONFIG[theme]:
                    errors.append(f"Warna '{color}' tidak ditemukan di THEME_CONFIG['{theme}']")
        else:
            errors.append(f"Tema '{theme}' tidak ditemukan di THEME_CONFIG")
    
    # Validasi font
    required_fonts = ['title_font', 'subtitle_font', 'body_font']
    for font in required_fonts:
        if font not in FONT_CONFIG:
            errors.append(f"Font '{font}' tidak ditemukan di FONT_CONFIG")
    
    # Validasi window
    if WINDOW_CONFIG['min_width'] <= 0 or WINDOW_CONFIG['min_height'] <= 0:
        errors.append("Ukuran window minimum harus lebih dari 0")
    
    if errors:
        raise ValueError(f"Konfigurasi tidak valid: {'; '.join(errors)}")
    
    return True

if __name__ == "__main__":
    # Test konfigurasi
    try:
        validate_config()
        print("✅ Konfigurasi valid")
        
        # Test beberapa konfigurasi
        print(f"Tema primary color: {get_config('theme', 'primary_color')}")
        print(f"Font title: {get_config('font', 'title_font')}")
        print(f"Window title: {get_config('window', 'title')}")
        
    except Exception as e:
        print(f"❌ Error konfigurasi: {e}")
