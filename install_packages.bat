@echo off
echo 📦 Instalando dependências do requirements.txt...

:: Verifica se o pip existe
where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ pip não encontrado. Instale o Python/pip primeiro.
    exit /b 1
)

pip install --upgrade pip
pip install -r requirements.txt

echo ✅ Instalação concluída!
pause