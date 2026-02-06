# Contributing to Cyber Coding Game

First off, thank you for considering contributing! 🎉

This project is meant to help beginners learn cybersecurity through coding, and your contribution could help hundreds of future cyber defenders.

---

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Development Setup](#development-setup)
4. [Submitting Changes](#submitting-changes)
5. [Style Guidelines](#style-guidelines)
6. [Security Guidelines](#security-guidelines)

---

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold a welcoming and inclusive environment.

---

## How Can I Contribute?

### 🐛 Report Bugs

Found something broken? [Open an issue](../../issues/new) with:

- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

### 💡 Suggest Features

Have an idea? We'd love to hear it! Open an issue with the "enhancement" label.

### 📝 Improve Documentation

See a typo? Something confusing? Documentation improvements are always welcome.

### 🎮 Create New Missions

Want to add a mission? Here's how:

1. Choose an appropriate tier (1=beginner, 2=intermediate, 3=advanced)
2. Create a markdown file in `lessons/tier{N}_*/`
3. Include: story, learning goals, task, solution, common mistakes
4. Submit a PR!

### 💻 Write Code

Check out issues labeled "good first issue" for beginner-friendly tasks.

---

## Development Setup

### Prerequisites

- Python 3.9+
- Node.js 18+
- Git

### Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/cyber-coding-game.git
cd cyber-coding-game

# Run setup script
# Windows:
scripts\dev_setup.bat

# Linux/macOS:
./scripts/dev_setup.sh
```

### Running Locally

```bash
# Start both servers
# Windows:
scripts\run_dev_server.bat

# Linux/macOS:
./scripts/run_dev_server.sh
```

- Backend: <http://localhost:8000>
- Frontend: <http://localhost:5173>

---

## Submitting Changes

1. **Fork the repo** and create a branch from `main`
2. **Make your changes** following our style guidelines
3. **Test your changes** locally
4. **Commit** with clear, descriptive messages
5. **Push** and open a Pull Request

### Commit Message Format

```
type: short description

Longer explanation if needed.
```

Types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

Example:

```
feat: add mission 11 covering password hashing

Introduces a new Tier 2 mission teaching secure password storage
with bcrypt. Includes hints for common mistakes.
```

---

## Style Guidelines

### Python (Backend)

- Follow PEP 8
- Use type hints where helpful
- Write docstrings for functions
- Keep functions small and focused

### JavaScript/React (Frontend)

- Use functional components and hooks
- Follow the existing component patterns
- Use CSS variables for theming
- Keep components focused

### Documentation

- Write for beginners
- Use simple language
- Include examples
- Explain the "why", not just the "how"

---

## Security Guidelines

### ⚠️ CRITICAL

This is a security education project. All contributions MUST:

1. **Never execute real code** — Sandbox services must remain simulated
2. **Never include real credentials** — Use placeholders only
3. **Never teach offensive techniques** — Focus on defense
4. **Validate all inputs** — Both frontend and backend
5. **Follow secure coding practices** — See `docs/secure-coding-standards.md`

### Before Submitting

Ask yourself:

- Could this be misused for attacks? If yes, redesign it
- Are there any hardcoded secrets? Remove them
- Is user input properly validated?

---

## Questions?

Feel free to open an issue with the "question" label. We're here to help!

Thank you for making cybersecurity education more accessible! 🛡️
