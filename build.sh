#!/bin/bash

# ==========================================
# CONFIGURACIÓN DEL PROYECTO
# ==========================================
APP_NAME="CorrectorDeLetras"
MAIN_SCRIPT="main.py"
ICON_FILE="./resources/icons/AppIcon.icns"
VERSION="1.0.0"

# ==========================================
# COMPILACIÓN PARA MACOS INTEL (x86_64)
# ==========================================
export MACOSX_DEPLOYMENT_TARGET=11.0

echo "🚀 Iniciando proceso de construcción para $APP_NAME (Intel x86_64)…"

# 1. Limpieza
echo "🧹 Limpiando archivos antiguos..."
rm -rf build dist
rm -f "$APP_NAME.spec"

# 2. Verificación de PyInstaller
echo "📦 Verificando herramientas de construcción..."
pip install --upgrade pyinstaller pyside6

# 3. Compilación SOLO PARA INTEL
echo "🔨 Compilando aplicación para x86_64…"

arch -x86_64 pyinstaller --noconfirm --clean \
    --name "$APP_NAME" \
    --windowed \
    --icon "$ICON_FILE" \
    --target-architecture x86_64 \
    --add-data "resources:resources" \
    "$MAIN_SCRIPT"

# 5. Finalización
if [ -d "dist/$APP_NAME.app" ]; then
    echo "✅ ¡Construcción exitosa!"
    echo "📁 Tu aplicación está en: dist/$APP_NAME.app"
    open dist/
else
    echo "❌ Hubo un error durante la construcción."
    exit 1
fi
