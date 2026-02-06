# Mission 07: Fix the Vulnerable Code 🔧

**Tier:** 🔴 Threat Hunter  
**Language:** Python  
**XP Reward:** 50  
**Badge:** Code Fixer

---

## 📖 Story Setup

> The security scanner flagged our user registration code.
>
> "There's a SQL injection vulnerability," your lead says. "Find it and fix it before attackers exploit it."

---

## 🎯 Learning Goals

### Coding Concept: Input Validation

Never trust user input. Always validate and sanitize data before using it.

### Security Concept: SQL Injection Prevention

SQL injection happens when user input becomes part of database commands. Use parameterized queries to prevent it.

---

## 📋 Your Task

Find the vulnerability and fix it.

### Vulnerable Code

```python
def create_user(username, email):
    # This code is INSECURE!
    query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
    database.execute(query)
    return "User created!"
```

### The Problem

If `username` is `admin'; DROP TABLE users; --`, the query becomes:

```sql
INSERT INTO users (username, email) VALUES ('admin'; DROP TABLE users; --', 'email')
```

This deletes the entire users table!

---

## ✅ Fixed Code

```python
def create_user(username, email):
    # SECURE: Using parameterized queries
    query = "INSERT INTO users (username, email) VALUES (?, ?)"
    database.execute(query, (username, email))
    return "User created!"
```

### Why This Works

- User input never becomes part of the SQL command
- The `?` placeholders separate code from data
- Database treats parameters as data only, never as commands

---

## 🎉 Success Message

> "You fixed it! SQL injection is one of the most dangerous and common vulnerabilities. You now know how to spot it AND how to prevent it. 🔧"

**[Badge Unlocked: Code Fixer]**
