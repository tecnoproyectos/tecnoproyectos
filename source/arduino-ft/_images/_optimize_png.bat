@set PATH=d:\Bin\imagetools;%PATH%

@for %%f in (arduino-ft-3*.png) do optipng -o 6 %%f

rem d:\Bin\ImageMagick\magick.exe arduino-ft-39.png arduino-ft-39.jpg
pause