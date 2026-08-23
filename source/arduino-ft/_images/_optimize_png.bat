@set PATH=d:\Bin\imagetools;%PATH%

@for %%f in (arduino-ft-*.png) do optipng -o 6 %%f

pause