# -*- mode: python ; coding: utf-8 -*-
# PCPasokh Internet Repair Simple - PyInstaller Spec File
# Specification file for building simple executable

block_cipher = None

a = Analysis(
    ['main_simple.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk', 
        'tkinter.scrolledtext',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'threading',
        'socket',
        'subprocess',
        'platform',
        'datetime',
        'uuid',
        'hashlib',
        'os'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        'customtkinter',
        'psutil',
        'requests',
        'ping3',
        'speedtest',
        'dns',
        'PIL'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PCPasokh_Internet_Repair_Simple',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version_info.py',
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)