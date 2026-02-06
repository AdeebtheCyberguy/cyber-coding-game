@echo off
REM ===========================================
REM Run Development Servers (Windows)
REM ===========================================
REM This script starts both backend and frontend
REM development servers.
REM ===========================================

echo ============================================
echo Cyber Coding Game - Starting Dev Servers
echo ============================================
echo.

REM Start Backend in new window
echo [1/2] Starting Backend Server...
start "Cyber Game - Backend" cmd /k "cd backend && venv\Scripts\activate && uvicorn app.main:app --reload --port 8000"
echo       Backend starting on http://localhost:8000
echo.

REM Wait a moment for backend to initialize
timeout /t 2 /nobreak >nul

REM Start Frontend in new window  
echo [2/2] Starting Frontend Server...
start "Cyber Game - Frontend" cmd /k "cd frontend && npm run dev"
echo       Frontend starting on http://localhost:5173
echo.

echo ============================================
echo Both servers are starting in separate windows!
echo.
echo   Backend API: http://localhost:8000
echo   Frontend UI: http://localhost:5173
echo.
echo Press Ctrl+C in each window to stop.
echo ============================================
