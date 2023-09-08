# flask-jinja2-cx_freeze-setup.py

2023, getting Flask to see `/templates/` and `/static/` jinja2 folders when compiling with `cx_freeze`

I just got this working and was too elated to clean up my code, there are better ways to handle paths. Either way, this should help you.

```python
td = Path(__file__).parent.parent.parent / 'templates'
sd = Path(__file__).parent.parent.parent / 'static'

app = Flask(__name__, template_folder=td.resolve(), static_folder=sd.resolve())
app.config.from_pyfile

```


setup.py (python setup.py build)

```python

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
```
