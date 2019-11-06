call activate py27

:: pip install pelican Markdown
:: pip install fabric

:: pelican content -s publishconf.py

fab regenerate
