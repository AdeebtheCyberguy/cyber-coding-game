# 🔒 Security Policy

## 🎯 Purpose of This Project

This game is for **defensive, educational purposes only**. 

Everything you learn here should be used to **protect systems**, not attack them. The skills you gain are valuable — please use them ethically.

---

## 🚨 Reporting Security Issues

Found a security bug? Thank you! Here's how to report it safely:

### Do This:
1. **Email us privately** at: `security@example.com` (replace with your actual email)
2. Include:
   - What the issue is
   - Steps to reproduce it
   - Your suggested fix (if you have one)

### Don't Do This:
- ❌ Don't post security issues publicly in GitHub Issues
- ❌ Don't exploit the issue on live systems
- ❌ Don't share the vulnerability before it's fixed

We'll respond within **48 hours** and keep you updated on the fix.

---

## 🔐 Security Rules for Contributors

### 1. Never Commit Secrets

**What are secrets?**
- API keys
- Passwords
- Tokens
- Private keys
- Database credentials

**Where should secrets go?**
- In `.env` files (which are in `.gitignore`)
- In environment variables
- NEVER in code files or commits

```bash
# ❌ BAD - Never do this!
API_KEY = "sk-abc123supersecret"

# ✅ GOOD - Use environment variables
import os
API_KEY = os.getenv("API_KEY")
```

### 2. Enable Two-Factor Authentication (2FA)

Protect your GitHub account:
1. Go to GitHub Settings → Password and Authentication
2. Enable Two-Factor Authentication
3. Save your recovery codes somewhere safe

### 3. Keep Dependencies Updated

Old libraries can have security holes. Run these regularly:

```bash
# Python
pip list --outdated
pip install --upgrade PACKAGE_NAME

# Node.js
npm outdated
npm update
```

### 4. Never Execute Untrusted Code

The sandboxes in this project are **simulations only**. They don't actually run user code.

If you're modifying the sandbox:
- ❌ Never use `eval()` or `exec()` on user input
- ❌ Never call `subprocess.run()` with user input
- ✅ Use whitelists and pattern matching instead

---

## 🛡️ What This Game Teaches (And Doesn't)

### ✅ We Teach:
- How to **detect** attacks in logs
- How to **fix** insecure code
- How to **think** like a defender
- Safe coding practices

### ❌ We Don't Teach:
- How to hack into systems you don't own
- How to exploit real vulnerabilities
- How to bypass security on live systems

---

## 📜 Ethical Use Statement

By using this project, you agree to:

1. **Only practice on systems you own** or have explicit written permission to test
2. **Never use these skills to harm** others or their systems
3. **Report vulnerabilities responsibly** when you find them
4. **Help others learn** to defend their systems

**Remember:** The goal is to be a *defender*, not an attacker. The world needs more people protecting systems, not breaking them.

---

## 🆘 Need Help?

If you're unsure whether something is safe or ethical:
- Ask in a GitHub Discussion
- Email the maintainers
- When in doubt, don't do it

---

<p align="center">
  <strong>Stay safe. Stay ethical. Stay curious.</strong> 🛡️
</p>
