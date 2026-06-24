@set PATH=d:\Bin\imagetools;%PATH%

@for %%f in (*.png) do optipng -o 6 %%f

pause