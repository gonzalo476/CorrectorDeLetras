#!/bin/bash

# ==========================================
# CONFIGURACIÓN DEL PROYECTO
# ==========================================
# Cambia estos valores por los de tu proyecto
APP_NAME="CorrectorDeLetras"
MAIN_SCRIPT="main.py"     # Tu archivo python principal
ICON_FILE="./resources/icons/AppIcon.icns"     # Tu archivo de icono (debe ser .icns para macOS)
VERSION="1.0.0"

# ==========================================
# CONFIGURACIÓN PARA MACOS BIG SUR (11.0) +
# ==========================================
# Esto le dice al compilador que el objetivo mínimo es Big Sur.
# Ayuda a evitar problemas de compatibilidad con librerías del sistema.
export MACOSX_DEPLOYMENT_TARGET=11.0

echo "🚀 Iniciando proceso de construcción para $APP_NAME..."

# 1. Limpieza de builds anteriores
echo "🧹 Limpiando archivos antiguos..."
rm -rf build dist
rm -f "$APP_NAME.spec"

# 2. Verificación de entorno virtual (Opcional pero recomendado)
# Si usas venv, descomenta las siguientes líneas:
# if [ -d "venv" ]; then
#     source venv/bin/activate
#     echo "✅ Entorno virtual activado."
# fi

# 3. Instalación/Actualización de dependencias de construcción
echo "📦 Verificando herramientas de construcción..."
pip install --upgrade pyinstaller pyside6

# 4. Ejecución de PyInstaller
# Explicación de banderas:
# --noconfirm: No pregunta antes de sobrescribir.
# --windowed: IMPORTANTE. Evita que salga la terminal negra al abrir la app.
# --onedir: Crea una carpeta. (Usa --onefile si quieres un solo ejecutable, pero onedir es más rápido al abrir).
# --clean: Limpia la caché de pyinstaller.
# --target-arch universal2: Intenta crear binarios para Intel y Apple Silicon (M1/M2/M3).
echo "🔨 Compilando aplicación..."

pyinstaller --noconfirm --clean \
    --name "$APP_NAME" \
    --windowed \
    --icon "$ICON_FILE" \
    --target-architecture universal2 \
    --add-data "resources:resources" \
    "$MAIN_SCRIPT"

# NOTA SOBRE --add-data:
# El formato es "origen:destino". 
# Si tienes una carpeta de imágenes llamada 'recursos', usa la línea de arriba.
# Si no tienes archivos extra, borra esa línea.

# 5. Finalización
if [ -d "dist/$APP_NAME.app" ]; then
    echo "✅ ¡Construcción exitosa!"
    echo "📁 Tu aplicación está en: dist/$APP_NAME.app"
    
    # Opcional: Abrir la carpeta al terminar
    open dist/
else
    echo "❌ Hubo un error durante la construcción."
    exit 1
fi