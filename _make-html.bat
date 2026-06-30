@echo off
set PATH=C:\Bin\miktex\texmfs\install\miktex\bin\x64;%PATH%
set PATH=%~dp0\venv\Scripts;%PATH%
call activate.bat

sphinx-build -b html -D language="es" source build/html
echo.
sphinx-build -b html -D language="en" source build/html/en
echo.
python source/_custom/sitemap.py "build/html"
pause

