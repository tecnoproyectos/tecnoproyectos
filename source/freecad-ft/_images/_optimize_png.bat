@set PATH=d:\Bin\imagetools;%PATH%

@for %%f in (freecad-ft-*.png) do optipng -o 7 %%f

pause