@echo off
chcp 65001 >nul

:: Activar soporte de ANSI en Windows (solo Win10+)
for /f "tokens=2 delims=: " %%i in ('"reg query HKEY_CURRENT_USER\Console /v VirtualTerminalLevel 2>nul"') do set vt=%%i
if not defined vt (
    reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul
)

:: Colores ANSI
set RED=[31m
set GREEN=[32m
set YELLOW=[33m
set BLUE=[34m
set CYAN=[36m
set RESET=[0m

:menu
cls
echo                %YELLOW%····································································%CYAN%
echo                %YELLOW%:                                                                  :%CYAN%
echo ─▄█▀█▄──▄███▄  %YELLOW%:   ░█▀▀░█░█░█▀▄░▀█▀░█▀▄░█▀█░█▀▄░░░█▀▄░█▀▀░░░█▀█░█▀█░▀█▀░█▀█░█▀▀   :%CYAN%─▄█▀█▄──▄███▄
echo ▐█░██████████▌ %YELLOW%:   ░▀▀█░█░█░█▀▄░░█░░█░█░█░█░█▀▄░░░█░█░█▀▀░░░█░█░█░█░░█░░█▀█░▀▀█   :%CYAN%▐█░██████████▌
echo ─██▒█████████  %YELLOW%:   ░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀░░▀▀▀░▀░▀░░░▀▀░░▀▀▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀   :%CYAN%─██▒█████████
echo ──▀████████▀   %YELLOW%:   ░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀▀░█▀█░█▀▄░░░▀▀█░█░█░█░░░▀█▀░█▀█░█▀█     :%CYAN%──▀████████▀
echo ─────▀██▀      %YELLOW%:   ░█▀▀░█▀▄░█░█░█▀▀░█▀▀░▀▀█░█░█░█▀▄░░░░░█░█░█░█░░░░█░░█▀█░█░█     :%CYAN%─────▀██▀
echo .──────▀.      %YELLOW%:   ░▀░░░▀░▀░▀▀▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀     :%CYAN%.──────▀.
echo                %YELLOW%:                                                                  :%CYAN%
echo                %YELLOW%····································································%CYAN%
echo %GREEN%............................................................................................................
echo :    1. Subir notas             :           2. Modificar notas               :            %RED%0. Salir%GREEN%         :
echo ............................................................................................................%RESET%
set /p opcion="Elige una opcion: "

if "%opcion%"=="1" (
    lector.exe
    pause
    goto menu
)

if "%opcion%"=="2" (
    notepad notas.txt
    goto menu
)

if "%opcion%"=="0" (
    echo Saliendo...
    exit
)

echo Opcion no valida
pause
goto menu
