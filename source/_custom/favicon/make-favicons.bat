@echo off
SET magick=\bin\imagemagick\convert.exe
SET optipng=\bin\imagetools\optipng.exe

%magick% favicon.png -resize 192x192  favicon-192.png
%magick% favicon.png -resize 96x96    favicon-96.png
%magick% favicon.png -resize 32x32    favicon-32.png

%optipng% favicon.png
%optipng% favicon-192.png
%optipng% favicon-96.png
%optipng% favicon-32.png

%magick% favicon-32.png favicon.ico

copy /Y favicon.ico     ..\extra\
copy /Y favicon-192.png ..\extra\
copy /Y favicon.png     ..\..\_static\

copy /Y favicon.ico     ..\..\..\..\test\template\static
copy /Y favicon-192.png ..\..\..\..\test\template\static

pause