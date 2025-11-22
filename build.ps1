# ==========================================
# CONFIGURACIÓN DEL PROYECTO
# ==========================================
$AppName = "CorrectorDeLetras"
$MainScript = "main.py"
# Asegúrate de que la ruta al icono sea correcta
$IconFile = "resources\icons\AppIcon.ico" 

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " INICIANDO CONSTRUCCION DE $AppName"
Write-Host " (Asumiendo entorno virtual activo)"
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Limpieza de builds anteriores
Write-Host "[1/3] Limpiando archivos antiguos..." -ForegroundColor Yellow
if (Test-Path "build") { Remove-Item -Path "build" -Recurse -Force }
if (Test-Path "dist") { Remove-Item -Path "dist" -Recurse -Force }
if (Test-Path "$AppName.spec") { Remove-Item -Path "$AppName.spec" -Force }

# 2. Instalación/Actualización de dependencias
Write-Host "[2/3] Verificando librerías..." -ForegroundColor Yellow
# Usa el pip del entorno actual
python -m pip install --upgrade pyinstaller pyside6

# 3. Ejecución de PyInstaller
Write-Host "[3/3] Compilando ejecutable..." -ForegroundColor Yellow

# Usamos el carácter ` (backtick) para dividir el comando en varias líneas en PowerShell
python -m PyInstaller --noconfirm --clean `
    --name "$AppName" `
    --windowed `
    --icon "$IconFile" `
    --add-data "resources;resources" `
    "$MainScript"

# 4. Verificación Final
$ExePath = "dist\$AppName\$AppName.exe"

if (Test-Path $ExePath) {
    Write-Host "`n==========================================" -ForegroundColor Cyan
    Write-Host " EXITO: Construcción completada." -ForegroundColor Green
    Write-Host " Ubicación: $ExePath" -ForegroundColor Gray
    Write-Host "==========================================" -ForegroundColor Cyan
    
    # Abre la carpeta dist
    Invoke-Item "dist\$AppName"
}
else {
    Write-Host "`n==========================================" -ForegroundColor Red
    Write-Host " ERROR: Algo salió mal durante la compilación." -ForegroundColor Red
    Write-Host "==========================================" -ForegroundColor Red
    Pause
}