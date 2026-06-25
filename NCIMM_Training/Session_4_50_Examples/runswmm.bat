@echo off
setlocal enabledelayedexpansion

echo ================================================
echo   EPA SWMM Batch Runner
echo ================================================
echo.

set "SWMM_PATH=C:\Program Files (x86)\EPA SWMM 5.2.4\runswmm.exe"

for %%f in (*.inp) do (
    echo Processing: %%f
    "%SWMM_PATH%" "%%f" "%%~nf.rpt" "%%~nf.out"
    echo.
)

echo ================================================
echo   All files processed!
echo ================================================
pause