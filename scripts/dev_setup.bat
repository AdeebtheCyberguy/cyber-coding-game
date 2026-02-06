@echo off
REM ===========================================
REM Development Setup Script for Windows
REM ===========================================
REM This script sets up your development environment
REM for the Cyber Coding Game.
REM ===========================================

echo ============================================
echo Cyber Coding Game - Development Setup
echo ============================================
echo.

REM Check Python
echo [1/4] Checking Python...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python not found. Please install Python 3.9+
    echo Download: https://www.python.org/downloads/
    exit /b 1
)
echo       Python found!
echo.

REM Check Node.js
echo [2/4] Checking Node.js...
node --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Node.js not found. Please install Node.js 18+
    echo Download: https://nodejs.org/
    exit /b 1
)
echo       Node.js found!
echo.

REM Setup Backend
echo [3/4] Setting up Backend...
cd backend
if not exist "venv" (
    echo       Creating virtual environment...
    python -m venv venv
)
echo       Activating virtual environment...
call venv\Scripts\activate.bat
echo       Installing dependencies...
pip install -r requirements.txt --quiet
cd ..
echo       Backend ready!
echo.

REM Setup Frontend
echo [4/4] Setting up Frontend...
cd frontend
echo       Installing npm packages...
call npm install --silent
cd ..
echo       Frontend ready!
echo.

echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo To start development:
echo   1. Backend:  cd backend ^& venv\Scripts\activate ^& uvicorn app.main:app --reload
echo   2. Frontend: cd frontend ^& npm run dev
echo.
echo Happy coding, cyber defender!
echo ============================================
