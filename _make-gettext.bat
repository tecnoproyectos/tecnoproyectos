@ECHO OFF
rem ********************
rem    MAKE GETTEXT
rem ********************

set PATH=%~dp0\venv\Scripts;%PATH%
call activate.bat

sphinx-build -b gettext source build/gettext

cd source
sphinx-intl update -p ../build/gettext -l en
cd ..

cp -f locale/en/sphinx.po  locale/en/LC_MESSAGES/sphinx.po
pause

