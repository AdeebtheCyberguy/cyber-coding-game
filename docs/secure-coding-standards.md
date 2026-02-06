# ✅ Secure Coding Standards

A simple checklist for writing safe code. Follow these rules to keep your code — and your users — secure!

---

## 🎯 The Golden Rules

1. **Never trust user input** — Always validate and sanitize
2. **Never store secrets in code** — Use environment variables
3. **Never give more access than needed** — Principle of least privilege
4. **Always handle errors safely** — Don't leak sensitive info

---

## 📋 The Checklist

### ✅ Input Validation

**Always validate everything that comes from users.**

```python
# ❌ DANGEROUS - Trusting user input
username = request.get("username")
query = f"SELECT * FROM users WHERE name = '{username}'"

# ✅ SAFE - Using parameterized queries
username = request.get("username")
query = "SELECT * FROM users WHERE name = ?"
database.execute(query, (username,))
```

**Rules:**
- [ ] Check data types (is it really a number?)
- [ ] Check lengths (username shouldn't be 10,000 characters)
- [ ] Check patterns (email should look like an email)
- [ ] Use allowlists when possible (only accept known-good values)

---

### ✅ Avoid Dangerous Functions

**Some functions can run arbitrary code. Avoid them!**

```python
# ❌ NEVER DO THIS
user_code = request.get("code")
eval(user_code)  # Runs whatever code the user sends!
exec(user_code)  # Same problem!

# ✅ INSTEAD
# Use specific, limited operations
# Or use safe sandbox simulations (like this game does!)
```

**Functions to avoid:**
| Language | Dangerous Functions |
|----------|---------------------|
| Python | `eval()`, `exec()`, `os.system()`, `subprocess.shell=True` |
| JavaScript | `eval()`, `Function()`, `setTimeout(string)` |
| Bash | Direct user input in commands |

---

### ✅ Handle Errors Safely

**Show users helpful errors, but never expose system details.**

```python
# ❌ DANGEROUS - Leaking internal information
try:
    result = database.query(user_data)
except Exception as e:
    return f"Error: {e}"  # Might show database structure, paths, etc.!

# ✅ SAFE - Generic user message, detailed internal log
try:
    result = database.query(user_data)
except Exception as e:
    logger.error(f"Database error: {e}")  # Log full details internally
    return "Something went wrong. Please try again."  # Generic to user
```

**Rules:**
- [ ] Never show stack traces to users
- [ ] Never reveal file paths, database schemas, or server info
- [ ] Log detailed errors internally for debugging
- [ ] Show friendly, generic messages to users

---

### ✅ Never Log Secrets

**Logs are often viewed by many people. Keep secrets out!**

```python
# ❌ DANGEROUS - Logging sensitive data
logger.info(f"User {username} logged in with password {password}")
logger.debug(f"API call with key: {api_key}")

# ✅ SAFE - Mask sensitive data
logger.info(f"User {username} logged in successfully")
logger.debug(f"API call with key: {api_key[:4]}****")
```

**Never log:**
- [ ] Passwords
- [ ] API keys
- [ ] Credit card numbers
- [ ] Personal identification numbers
- [ ] Session tokens

---

### ✅ Use Environment Variables for Secrets

**Never hardcode secrets in your source code!**

```python
# ❌ DANGEROUS - Secret in code (will end up in Git!)
API_KEY = "sk-1234567890abcdef"

# ✅ SAFE - Load from environment
import os
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable is required")
```

**How to use .env files:**
1. Create `.env` file (make sure it's in `.gitignore`!)
2. Add secrets: `API_KEY=sk-1234567890abcdef`
3. Load with `python-dotenv` or similar library

---

### ✅ Principle of Least Privilege

**Only give the minimum access needed.**

```python
# ❌ BAD - Running everything as admin
database.connect(user="root", password="admin123")

# ✅ GOOD - Use a limited user
database.connect(user="app_readonly", password=os.getenv("DB_PASS"))
```

**Apply to:**
- [ ] Database users (read-only when possible)
- [ ] File permissions (don't make everything world-readable)
- [ ] API keys (use scoped tokens with limited permissions)
- [ ] User accounts (admins vs regular users)

---

### ✅ Keep Dependencies Updated

**Old libraries often have known security holes.**

```bash
# Check for outdated packages

# Python
pip list --outdated
pip-audit  # Security-specific audit

# Node.js
npm outdated
npm audit
```

**Rules:**
- [ ] Run security audits regularly
- [ ] Update dependencies monthly (or when security issues are found)
- [ ] Use tools like Dependabot to automate updates
- [ ] Review changelogs before updating major versions

---

### ✅ Avoid Shell Execution

**Never run shell commands with user input!**

```python
# ❌ EXTREMELY DANGEROUS
import os
filename = request.get("filename")
os.system(f"cat {filename}")  # User could input "; rm -rf /"

# ❌ STILL DANGEROUS (even with subprocess)
import subprocess
subprocess.run(f"cat {filename}", shell=True)

# ✅ SAFER - Use Python libraries directly
with open(filename, 'r') as f:  # Still need to validate filename!
    content = f.read()

# ✅ SAFEST - Validate against allowlist
ALLOWED_FILES = {"readme.txt", "log.txt", "data.json"}
if filename in ALLOWED_FILES:
    with open(filename, 'r') as f:
        content = f.read()
else:
    raise ValueError("File not allowed")
```

---

### ✅ Encode Output Properly

**Prevent cross-site scripting (XSS) by encoding output.**

```javascript
// ❌ DANGEROUS - Inserting user input directly into HTML
element.innerHTML = userComment;  // What if userComment is "<script>evil()</script>"?

// ✅ SAFE - Use text content or proper encoding
element.textContent = userComment;  // Treats it as text, not HTML

// ✅ SAFE - Or escape HTML entities
function escapeHtml(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
element.innerHTML = escapeHtml(userComment);
```

---

## 🚀 Quick Reference

**Before any code goes live, ask:**

| Check | Question |
|-------|----------|
| 🔒 | Did I validate all user input? |
| 🚫 | Am I avoiding `eval` and shell execution? |
| 📝 | Do my error messages hide sensitive details? |
| 🔑 | Are all secrets in environment variables, not code? |
| 📋 | Am I logging carefully without secrets? |
| ⬇️ | Are my dependencies up to date? |
| 🔐 | Am I using least privilege? |
| 💉 | Am I using parameterized queries for databases? |
| 🌐 | Am I encoding output to prevent XSS? |

---

## 📚 Learn More

- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — Detailed secure coding guides
- [CWE Top 25](https://cwe.mitre.org/top25/) — Most dangerous software weaknesses
- [SANS Secure Coding](https://www.sans.org/secure-coding/) — Training and resources

---

<p align="center">
  <strong>Secure code protects everyone. Make it a habit! 🛡️</strong>
</p>
