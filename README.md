# 🛡️ Cyber Coding Game

**Learn cybersecurity through coding — even if you've never written a single line of code before.**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-brightgreen.svg)](#)
[![Safe & Ethical](https://img.shields.io/badge/Safe-Educational%20Only-blue.svg)](#)

---

## 🌟 What Is This?

Cyber Coding Game is a **free, fun way to learn cybersecurity** by actually doing it. You'll write real code (Python, Bash, JavaScript) and search through logs like a real security analyst — all in a **completely safe, simulated environment**.

### 🎮 The Journey: Noob → Pro

| Level | You Are | What You'll Do |
|-------|---------|----------------|
| 🟢 **New Trainee** | Complete beginner | Click buttons, fill in blanks, learn what "code" even means |
| 🟡 **Analyst** | Getting comfortable | Write small scripts, search logs, spot suspicious stuff |
| 🔴 **Threat Hunter** | Confident defender | Investigate incidents, fix security bugs, think like a pro |

**No experience required.** We start with "Hello, World!" and take you all the way to investigating fake cyber attacks.

---

## 🚀 Quick Start (For Complete Beginners)

### Step 1: Install the Tools

You need two programs. Don't worry — they're free and safe!

**Git** (to download projects):
- Windows: Download from [git-scm.com](https://git-scm.com/download/win) → Run installer → Click "Next" on everything

**Node.js** (to run the game):
- Download from [nodejs.org](https://nodejs.org/) → Pick the "LTS" version → Run installer

**Python** (for the backend):
- Download from [python.org](https://www.python.org/downloads/) → Run installer → ✅ Check "Add Python to PATH"

### Step 2: Download This Project

Open **Command Prompt** (press `Win + R`, type `cmd`, press Enter) and paste this:

```bash
git clone https://github.com/YOUR_USERNAME/cyber-coding-game.git
cd cyber-coding-game
```

### Step 3: Run the Game

**Windows (PowerShell):**
```powershell
# Start the backend
cd backend
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000

# In a NEW terminal, start the frontend
cd frontend
npm install
npm run dev
```

### Step 4: Play!

Open your browser and go to: **http://localhost:5173**

That's it! You're ready to become a cyber defender! 🎉

---

## 📖 How the Game Works

### 🟢 Tier 1: New Trainee (You Know Nothing — And That's OK!)

When you first start, we assume you've **never coded before**. Every mission:

- Uses **simple words** (no scary jargon)
- Explains **every new concept** with examples
- Starts with **clicking and filling blanks** before you type code
- Gives **friendly hints** when you make mistakes
- Celebrates **every small win** with badges and encouragement

**Example Mission:** *"Your First Line of Code"*
> We'll show you exactly what to type. You'll see your code run. You'll feel like a hacker (the good kind)!

### 🟡 Tier 2: Analyst (Building Real Skills)

Now you're writing actual scripts:

- Count failed login attempts with Python
- Search logs with commands like `grep` 
- Spot suspicious patterns (weird IPs, odd times)
- Hints are available but less detailed

**Example Mission:** *"Who's Trying to Break In?"*
> Write a Python script that counts how many times someone failed to log in. If it's over 5 times... that's suspicious!

### 🔴 Tier 3: Threat Hunter (Think Like a Defender)

You're investigating incidents now:

- Combine multiple tools to solve mysteries
- Fix actual security bugs in code
- Minimal hints — you've got this!
- Feel the satisfaction of a real analyst

**Example Mission:** *"The Midnight Breach"*
> At 3 AM, someone accessed the server. Your job: figure out who, how, and what they touched. Use everything you've learned.

---

## 🛡️ Safety First

### This Game is 100% Safe

- **No real systems** are ever touched
- All code runs in a **fake, sandboxed environment**
- You **cannot break anything** — experiment freely!
- This is **defense training only**

### For Contributors

> ⚠️ **NEVER commit secrets** (passwords, API keys, tokens) to this repository  
> ⚠️ **NEVER use these skills** on systems you don't own  
> ⚠️ Keep your local tools updated

See [SECURITY.md](SECURITY.md) for full security guidelines.

---

## 📁 Project Structure

```
cyber-coding-game/
├── 📄 README.md          ← You are here!
├── 🔒 SECURITY.md        ← Security guidelines
├── 📜 LICENSE            ← MIT License (free to use)
│
├── 📂 docs/              ← Detailed documentation
├── 📂 backend/           ← Python API (powers the game)
├── 📂 frontend/          ← React website (what you see)
├── 📂 lessons/           ← All mission content
├── 📂 samples/           ← Example code to learn from
└── 📂 scripts/           ← Helper scripts for setup
```

---

## 🤝 Contributing

We'd love your help! Whether you're fixing typos, adding missions, or improving the UI — all contributions are welcome.

1. Fork this repository
2. Create a branch (`git checkout -b my-feature`)
3. Make your changes
4. Submit a Pull Request

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) first.

---

## 💚 Why We Made This

Cybersecurity can feel intimidating. Terms like "SQL injection" and "buffer overflow" sound scary. But here's the truth:

**Everyone starts as a beginner.**

This game exists to make that starting point as welcoming as possible. No judgment. No pressure. Just learning, one mission at a time.

*Welcome to the team, future defender.* 🛡️

---

## 📜 License

MIT License — free to use, modify, and share. See [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>Made with 💚 for future cyber defenders everywhere</strong>
</p>
