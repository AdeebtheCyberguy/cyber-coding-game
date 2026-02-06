# Mission 04: Build a Log Scanner 🔍

**Tier:** 🟡 Analyst  
**Language:** Python  
**XP Reward:** 25  
**Badge:** Pattern Finder

---

## 📖 Story Setup

> Your team lead approaches with an urgent task.
>
> "We need a Python script that counts failed login attempts per user," they explain. "If someone fails more than 5 times, that's suspicious — it could be an attacker guessing passwords."
>
> "Can you build it? This will be your first real security tool."

---

## 🎯 Learning Goals

### Coding Concept: Loops and Conditionals

- **Loops** let you repeat actions for each item in a list
- **Conditionals** let you make decisions based on data
- **Dictionaries** store data with labels (like `user: count`)

### Security Concept: Brute Force Detection

A brute force attack is when someone tries many passwords hoping one works. Detecting multiple failures from the same user or IP is a key defensive technique.

---

## 📋 Your Task

Write a Python script that:

1. Loops through log entries
2. Counts failed logins per user
3. Prints an alert if any user has more than 5 failures

---

## Starter Code

```python
logs = [
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "sarah", "status": "success"},
]

# Your code below:
# 1. Create a dictionary to count failures
# 2. Loop through each log entry
# 3. If status is "failed", increment the count
# 4. Check if any user has more than 5 failures
```

---

## ✅ Correct Solution

```python
logs = [
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "sarah", "status": "success"},
]

# Count failed logins per user
failed_counts = {}

for entry in logs:
    if entry["status"] == "failed":
        user = entry["user"]
        if user in failed_counts:
            failed_counts[user] += 1
        else:
            failed_counts[user] = 1

# Alert on suspicious activity
for user, count in failed_counts.items():
    if count > 5:
        print(f"⚠️ ALERT: {user} has {count} failed logins!")
```

**Output:** `⚠️ ALERT: john has 6 failed logins!`

---

## ❌ Common Mistakes

### Mistake 1: Checking for wrong value

```python
if entry["status"] == "fail":  # ❌ "fail" not "failed"
```

### Mistake 2: Not initializing the count

```python
failed_counts[user] += 1  # ❌ Error if user not in dict yet
```

### Mistake 3: Wrong comparison operator

```python
if count > "5":  # ❌ Comparing number to string
```

---

## 🎉 Success Message

> "Excellent work, Analyst! You just built a real brute force detector. This same logic powers security tools used by professionals worldwide. You're writing code that actually protects systems! 🔍"

**[Badge Unlocked: Pattern Finder]**
