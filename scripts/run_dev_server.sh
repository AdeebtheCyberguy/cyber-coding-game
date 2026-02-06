#!/bin/bash
# ===========================================
# Run Development Servers (Linux/macOS)
# ===========================================
# This script starts both backend and frontend
# development servers.
# ===========================================

echo "============================================"
echo "🛡️ Cyber Coding Game - Starting Dev Servers"
echo "============================================"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "Stopping servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start Backend
echo "[1/2] Starting Backend Server..."
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..
echo "      Backend running on http://localhost:8000 (PID: $BACKEND_PID)"
echo ""

# Wait for backend to initialize
sleep 2

# Start Frontend
echo "[2/2] Starting Frontend Server..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..
echo "      Frontend running on http://localhost:5173 (PID: $FRONTEND_PID)"
echo ""

echo "============================================"
echo "✅ Both servers are running!"
echo ""
echo "   Backend API: http://localhost:8000"
echo "   Frontend UI: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both servers."
echo "============================================"

# Wait for both processes
wait
