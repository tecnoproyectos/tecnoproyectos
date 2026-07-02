@echo off
rem MAKE GETTEXT

set PATH=%~dp0venv\Scripts;%PATH%
call "%~dp0venv\Scripts\activate.bat"

sphinx-build -b gettext source build/gettext
sphinx-intl -c source/conf.py update -l en

copy /Y  locale\en\sphinx.po  locale\en\LC_MESSAGES\sphinx.po
pause

