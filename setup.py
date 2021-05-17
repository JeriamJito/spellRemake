from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('controlaTelaPrincipal.py', base=base, target_name = 'Spell Remake')
]

setup(name='Spell Remake',
      version = '0.01',
      description = 'Jogo pra aprender inglês',
      options = {'build_exe': build_options},
      executables = executables)
