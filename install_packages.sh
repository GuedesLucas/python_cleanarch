#!/usr/bin/env bash
set -e

echo "📦 Instalando dependências do requirements.txt..."

# Verifica se pip está disponível
if ! command -v pip &> /dev/null; then
    echo "❌ pip não encontrado. Instale o Python/pip primeiro."
    exit 1
fi

pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Instalação concluída!"