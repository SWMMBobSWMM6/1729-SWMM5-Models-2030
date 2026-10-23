@echo off
setlocal enabledelayedexpansion

rem --- process the current folder plus every subfolder ---
for /d /r %%d in (.) do (
    rem only ask about folders that actually contain .inp files
    if exist "%%d\*.inp" (
        set "ans="
        set /p "ans=Run directory "%%~fd" ? [Y/N] "
        if /i "!ans!"=="Y" (
            for %%f in ("%%d\*.inp") do (
                echo Processing "%%f"
                "C:\Program Files (x86)\EPA SWMM 5.2.4\runswmm.exe" "%%f" "%%~dpf%%~nf.rpt" "%%~dpf%%~nf.out"
            )
        ) else (
            echo Skipping "%%~fd"
        )
    )
)
pause