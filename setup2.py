from cx_Freeze import setup, Executable

import sys
# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'temEatsss.exe')
]

data_files = [
   ("templates/", "templates/"), ("static/", "static/"), "mydatabase.db"
]


build_options = {'packages': ["os", "sys"],  'excludes': [], "include_msvcr": True, "includes": ["jinja2", "jinja2.ext", "pathlib", "flask", "pkg_resources"], "include_files": data_files}


setup(name='teMeats',
      version = '1.0',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
