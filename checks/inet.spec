# -*- mode: python -*-

block_cipher = None

a1 = Analysis(['check_internet.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=['logging.config'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz1 = PYZ(a1.pure, a1.zipped_data,
          cipher=block_cipher)

exe1 = EXE(pyz1,
          a1.scripts,
          [],
          exclude_binaries=True,
          name='check_internet',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)

coll1 = COLLECT(exe1,
               a1.binaries,
               a1.zipfiles,
               a1.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='check_internet')
