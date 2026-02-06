# 🎮 Cyber Coding Game - Overview

## 🌟 What Is This Project?

Cyber Coding Game is an **educational web application** that teaches cybersecurity through hands-on coding missions. Players learn Python, JavaScript, Bash, and log analysis by completing progressively challenging tasks in a safe, simulated environment.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │  HomePage   │  │MissionList  │  │MissionDetail│          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│         │               │               │                    │
│  ┌──────┴───────────────┴───────────────┴──────┐            │
│  │              React + Vite                    │            │
│  │         Premium Dark Theme UI                │            │
│  └──────────────────────────────────────────────┘            │
└─────────────────────────┬───────────────────────────────────┘
                          │ HTTP API
┌─────────────────────────┴───────────────────────────────────┐
│                        BACKEND                               │
│  ┌──────────────────────────────────────────────┐           │
│  │              FastAPI (Python)                 │           │
│  └──────────────────────┬───────────────────────┘           │
│                         │                                    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │   Python    │  │    Bash     │  │   Lucene    │          │
│  │   Sandbox   │  │   Sandbox   │  │   Search    │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│         ↓               ↓               ↓                    │
│  ┌──────────────────────────────────────────────┐           │
│  │     SAFE SIMULATION - No real execution!     │           │
│  └──────────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Core Concepts

### The "Noob to Pro" Philosophy

1. **Meet players where they are** — assume zero knowledge initially
2. **Gradual complexity** — start with clicking, progress to coding
3. **Safe experimentation** — mistakes are learning opportunities, not failures
4. **Contextual learning** — every coding concept connects to a security concept

### Three-Tier Progression

| Tier | Name | Focus |
|------|------|-------|
| 🟢 1 | New Trainee | Foundations: What is code? What are logs? |
| 🟡 2 | Analyst | Application: Write scripts to solve simple security tasks |
| 🔴 3 | Threat Hunter | Integration: Combine skills for realistic investigations |

---

## 🔒 Security by Design

This project is built with security in mind:

- **No real code execution** — sandboxes simulate, don't execute
- **Input validation everywhere** — size limits, pattern blocking
- **No secrets in code** — environment variables only
- **Educational focus** — defense, never offense

---

## 📁 Folder Structure

| Folder | Purpose |
|--------|---------|
| `/backend` | Python FastAPI server with sandbox services |
| `/frontend` | React + Vite web application |
| `/docs` | Detailed documentation |
| `/lessons` | Mission content organized by tier |
| `/samples` | Example code for learning |
| `/scripts` | Development helper scripts |

---

## 🚀 Quick Links

- [Getting Started](getting-started.md) — Setup instructions
- [Game Design](game-design.md) — Detailed mission breakdown
- [Cybersecurity Notes](cybersecurity-notes.md) — Concepts explained
- [Secure Coding Standards](secure-coding-standards.md) — Best practices

---

## 🤝 Contributing

See the main [README](../README.md) for contribution guidelines.

We especially welcome:
- 🎓 New mission ideas
- 🌍 Translations
- 🎨 UI improvements
- 📝 Documentation fixes
