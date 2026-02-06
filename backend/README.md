# 🐍 Backend - Cyber Coding Game API

This is the Python backend that powers the Cyber Coding Game. It provides APIs for missions, safe code execution simulation, and log searching.

---

## 🛡️ Security Notice

> ⚠️ **This backend does NOT execute real user code!**
>
> All "code execution" is **simulated** for educational purposes. The sandbox services use pattern matching and pre-defined outputs — they never call `eval()`, `exec()`, or run real shell commands.

---

## 🚀 Quick Setup

### 1. Create a Virtual Environment

```powershell
# Windows PowerShell
cd backend
python -m venv venv
.\venv\Scripts\Activate

# You should see (venv) at the start of your prompt
```

```bash
# Linux/Mac
cd backend
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
python -m uvicorn app.main:app --reload --port 8000
```

The API will be available at: `http://localhost:8000`

### 4. View API Documentation

FastAPI automatically creates docs! Visit:

- **Swagger UI:** <http://localhost:8000/docs>
- **ReDoc:** <http://localhost:8000/redoc>

---

## 📁 Folder Structure

```
backend/
├── README.md           ← You are here!
├── requirements.txt    ← Python dependencies
└── app/
    ├── __init__.py     ← Package marker
    ├── main.py         ← FastAPI application and routes
    ├── models.py       ← Pydantic data models
    ├── game_logic.py   ← Mission validation and progress
    └── services/
        ├── sandbox_python.py    ← Safe Python simulation
        ├── sandbox_bash.py      ← Safe Bash simulation
        └── lucene_search_sim.py ← Log search simulation
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/missions` | List all available missions |
| GET | `/api/missions/{id}` | Get mission details |
| POST | `/api/run/python` | Simulate Python code |
| POST | `/api/run/bash` | Simulate Bash commands |
| POST | `/api/search/logs` | Execute Lucene-style search |
| GET | `/api/progress` | Get player progress |
| POST | `/api/progress/complete` | Mark mission as complete |

---

## 🧪 Running Tests

```bash
# Install test dependencies (if not included)
pip install pytest pytest-asyncio

# Run tests
pytest -v
```

---

## 📦 Dependency Management

**Keep dependencies updated** to avoid security vulnerabilities:

```bash
# Check for outdated packages
pip list --outdated

# Update a specific package
pip install --upgrade PACKAGE_NAME

# Audit for security issues (install pip-audit first)
pip install pip-audit
pip-audit
```

---

## ⚙️ Environment Variables

Create a `.env` file in the `backend/` folder for local configuration:

```env
# Example .env file (NEVER commit this!)
DEBUG=true
SECRET_KEY=your-local-dev-secret-key
```

**Remember:** The `.env` file is in `.gitignore` and should NEVER be committed!

---

## 🆘 Troubleshooting

### "Module not found"

Make sure your virtual environment is activated:

```powershell
.\venv\Scripts\Activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### "Port already in use"

Use a different port:

```bash
python -m uvicorn app.main:app --reload --port 8001
```

### "UnicodeDecodeError on Windows"

Make sure your files are saved as UTF-8.

---

## 🤝 Contributing

When modifying the backend:

1. **Never use `eval()` or `exec()`** on user input
2. **Never run real shell commands** with user input
3. **Always validate input** before processing
4. **Add tests** for new functionality
5. **Update this README** if you add new endpoints
