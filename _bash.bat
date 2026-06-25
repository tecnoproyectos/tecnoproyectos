@echo off
set PATH=\Bin\cygwin64\bin;%PATH%
set PATH=%~dp0\venv\Scripts;%PATH%
call activate.bat
set PATH=\Bin\miktex\miktex\bin\x64;%PATH%
bash.exe