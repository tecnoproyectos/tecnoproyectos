@echo off
rem MAKE HTML PAGES

set PATH=%~dp0venv\Scripts;%PATH%
call "%~dp0venv\Scripts\activate.bat"
set PATH=C:\Bin\miktex\miktex\bin\x64;%PATH%

sphinx-build -b html -D language="es" source build/html
echo.
sphinx-build -b html -D language="en" source build/html/en
echo.
python source/_custom/sitemap.py "build/html"
pause

