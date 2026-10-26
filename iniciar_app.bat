@echo off
title Generador de Modelos Dimensionales en Estrella
cd /d "%~dp0"
cls
echo ============================================================
echo   INICIANDO GENERADOR DIMENSIONAL EN ESTRELLA
echo ============================================================
echo.
echo Iniciando servidor y abriendo tu navegador con el diseno nuevo...
echo.
python server.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [INFO] Abriendo directamente el archivo en tu navegador...
    start "" "index.html"
)
pause
