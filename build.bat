@echo off
TITLE Construyendo Aplicacion Python

REM ==========================================
REM CONFIGURACIÓN DEL PROYECTO
REM ==========================================
set APP_NAME=CorrectorDeLetras
set MAIN_SCRIPT=main.py
REM IMPORTANTE: En Windows el icono debe ser .ico
set ICON_FILE=resources\icons\AppIcon.ico
set VERSION=1.0.0

echo ==========================================
echo  INICIANDO CONSTRUCCION DE %APP_NAME%
echo ==========================================

REM 1. Limpieza de builds anteriores
echo [1/4] Limpiando archivos antiguos...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "%APP_NAME%.spec" del "%APP_NAME%.spec"

REM 2. Verificación de entorno (Opcional, descomentar si usas venv)
REM if exist "venv\Scripts\activate.bat" (
REM     call venv\Scripts\activate.bat
REM     echo [INFO] Entorno virtual activado.
REM )

REM 3. Instalación/Actualización de dependencias
echo [2/4] Verificando librerias...
pip install --upgrade pyinstaller pyside6

REM 4. Ejecución de PyInstaller
REM --noconfirm: Sobrescribe sin preguntar
REM --windowed: Sin consola negra (GUI)
REM --icon: Ruta al icono .ico
REM --add-data: Nota el separador ";" (punto y coma) para Windows
echo [3/4] Compilando ejecutable...

pyinstaller --noconfirm --clean ^
    --name "%APP_NAME%" ^
    --windowed ^
    --icon "%ICON_FILE%" ^
    --add-data "resources;resources" ^
    "%MAIN_SCRIPT%"

REM 5. Verificación Final
if exist "dist\%APP_NAME%\%APP_NAME%.exe" (
    echo.
    echo ==========================================
    echo  EXITO: Construccion completada.
    echo  Ubicacion: dist\%APP_NAME%\%APP_NAME%.exe
    echo ==========================================
    echo.
    REM Abre la carpeta dist
    explorer "dist\%APP_NAME%"
) else (
    echo.
    echo ==========================================
    echo  ERROR: Algo salio mal.
    echo ==========================================
    pause
)