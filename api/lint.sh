#!/bin/bash

echo "🔍 Running flake8..."
flake8 . || echo "⚠️ flake8 failed"

echo "🧹 Running black check..."
black . --check || echo "⚠️ black check failed"

echo "🔎 Running mypy..."
if command -v mypy &> /dev/null; then
    mypy . || echo "⚠️ mypy failed"
else
    echo "❌ mypy not installed"
fi

echo "✅ Linting completed (with possible warnings)."
