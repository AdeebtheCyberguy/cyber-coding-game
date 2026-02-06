# 🚀 Getting Started

This guide will help you set up the Cyber Coding Game on your computer. Written for complete beginners!

---

## 📋 What You'll Need

Before we start, you need to install a few free programs:

### 1. Git (Version Control)

Git lets you download projects from GitHub.

**Windows:**
1. Go to [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the installer
3. Run it and click "Next" on every screen (defaults are fine!)
4. When done, restart your computer

**To check it worked:**
Open Command Prompt (Win + R, type `cmd`, press Enter) and type:
```bash
git --version
```
You should see something like `git version 2.43.0`

---

### 2. Python (Backend Language)

**Windows:**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click the big yellow "Download Python" button
3. Run the installer
4. ⚠️ **IMPORTANT:** Check the box that says "Add Python to PATH"
5. Click "Install Now"

**To check it worked:**
```bash
python --version
```
You should see something like `Python 3.11.0`

---

### 3. Node.js (Frontend Tools)

**Windows:**
1. Go to [nodejs.org](https://nodejs.org/)
2. Download the **LTS** version (the one on the left)
3. Run the installer
4. Click "Next" on every screen

**To check it worked:**
```bash
node --version
npm --version
```
You should see version numbers for both.

---

## 📥 Download the Project

Now let's get the code! Open Command Prompt and run:

```bash
# Go to where you want the project
cd C:\Users\YourName\Documents

# Download the project
git clone https://github.com/YOUR_USERNAME/cyber-coding-game.git

# Go into the project folder
cd cyber-coding-game
```

---

## 🔧 Set Up the Backend

The backend is the Python server that powers the game.

### Step 1: Create a Virtual Environment

A virtual environment keeps this project's packages separate from other Python projects.

```powershell
# Go to the backend folder
cd backend

# Create the virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate

# You should see (venv) at the start of your command line!
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all the Python packages the backend needs.

### Step 3: Run the Backend

```bash
python -m uvicorn app.main:app --reload --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

**Leave this terminal open!** The backend needs to keep running.

---

## 🎨 Set Up the Frontend

The frontend is the website you'll see in your browser.

### Step 1: Open a New Terminal

Don't close the backend terminal! Open a new one.

### Step 2: Go to the Frontend Folder

```bash
cd C:\Users\YourName\Documents\cyber-coding-game\frontend
```

### Step 3: Install Dependencies

```bash
npm install
```

This downloads all the JavaScript packages.

### Step 4: Run the Frontend

```bash
npm run dev
```

You should see:
```
  VITE v5.0.0  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: http://192.168.1.100:5173/
```

---

## 🎮 Play the Game!

Open your web browser and go to:

**http://localhost:5173**

You should see the Cyber Coding Game homepage! 🎉

---

## 🆘 Troubleshooting

### "python is not recognized"
- Make sure you checked "Add Python to PATH" during installation
- Restart your computer and try again

### "npm is not recognized"
- Make sure Node.js is fully installed
- Restart your computer and try again

### "Port already in use"
- Another program is using that port
- Try a different port: `--port 8001` for backend, or close other programs

### "ModuleNotFoundError"
- Make sure your virtual environment is activated
- You should see `(venv)` at the start of your command line
- Run `pip install -r requirements.txt` again

### "npm install failed"
- Delete the `node_modules` folder
- Delete `package-lock.json`
- Run `npm install` again

---

## 🎓 What's Next?

Now that you're running the game:

1. **Start with Mission 1** — Learn your first code!
2. **Take your time** — There's no rush
3. **Make mistakes** — That's how you learn
4. **Have fun** — You're becoming a cyber defender! 🛡️

---

## 📚 More Resources

- [Overview](overview.md) — Understand the architecture
- [Game Design](game-design.md) — See all missions
- [Cybersecurity Notes](cybersecurity-notes.md) — Learn the concepts
