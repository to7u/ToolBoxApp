@echo off

set HH=%date:~2,2%
set MM=%date:~5,2%
set DD=%date:~8,2%
rem echo %HH%%MM%%DD%

set filetime=%time: =0%
set ho=%filetime:~0,2%
set mi=%filetime:~3,2%
set se=%filetime:~6,2%
rem echo %ho%%mi%%se%

set filename=%HH%%MM%%DD%_%ho%%mi%%se%

mkdir log\%filename%

ipconfig /all > log\%filename%\ipconfig_%filename%_bifore.txt

echo "dynamic-ip.bat"

ipconfig /all > log\%filename%\ipconfig_%filename%_after.txt

