#!/bin/bash
# ===========================================
# Development Setup Script for Linux/macOS
# ===========================================
# This script sets up your development environment
# for the Cyber Coding Game.
# ===========================================

set -e

echo "============================================"
echo "🛡️ Cyber Coding Game - Development Setup"
echo "============================================"
echo ""

# Check Python
echo "[1/4] Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not found. Please install Python 3.9+"
    exit 1
fi
echo "      ✓ Python found: $(python3 --version)"
echo ""

# Check Node.js
echo "[2/4] Checking Node.js..."
if ! command -v node &> /dev/null; then
    echo "[ERROR] Node.js not found. Please install Node.js 18+"
    exit 1
fi
echo "      ✓ Node.js found: $(node --version)"
echo ""

# Setup Backend
echo "[3/4] Setting up Backend..."
cd backend
if [ ! -d "venv" ]; then
    echo "      Creating virtual environment..."
    python3 -m venv venv
fi
echo "      Activating virtual environment..."
source venv/bin/activate
echo "      Installing dependencies..."
pip install -r requirements.txt --quiet
cd ..
echo "      ✓ Backend ready!"
echo ""

# Setup Frontend
echo "[4/4] Setting up Frontend..."
cd frontend
echo "      Installing npm packages..."
npm install --silent
cd ..
echo "      ✓ Frontend ready!"
echo ""

echo "============================================"
echo "✅ Setup Complete!"
echo "============================================"
echo ""
echo "To start development:"
echo "  1. Backend:  cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
echo "  2. Frontend: cd frontend && npm run dev"
echo ""
echo "Happy coding, cyber defender! 🛡️"
echo "============================================"
