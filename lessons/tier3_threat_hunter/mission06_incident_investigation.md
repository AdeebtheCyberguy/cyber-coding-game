# Mission 06: The Midnight Breach 🌙

**Tier:** 🔴 Threat Hunter  
**Language:** Python/Multi-tool  
**XP Reward:** 50  
**Badge:** Night Detective

---

## 📖 Story Setup

> 🚨 **ALERT**: Unusual activity detected at 3:17 AM
>
> Someone accessed the database server during off-hours. The SIEM flagged it, but now we need answers:
>
> - **Who** was it?
> - **How** did they get in?
> - **What** did they access?
>
> This is your investigation. Use everything you've learned.

---

## 🎯 Learning Goals

### Coding Concept: Multi-Tool Investigation

Real investigations combine:

- Log searches (Lucene)
- Command-line analysis (Bash)
- Data processing (Python)

### Security Concept: Incident Response

When something suspicious happens, we investigate systematically:

1. **Identify** - What triggered the alert?
2. **Scope** - How far did it spread?
3. **Contain** - Stop ongoing damage
4. **Document** - Record everything

---

## 📋 Your Task

1. Search logs for events around 3:17 AM
2. Trace the attacker's path
3. Identify what data was accessed
4. Document your findings

---

## Investigation Steps

### Step 1: Find the initial alert

```
hour:3 action:*access*
```

### Step 2: Trace back authentication

```python
# Look for login events before 3:17
for log in logs:
    if "03:1" in log["timestamp"]:
        print(log)
```

### Step 3: Build the timeline

Combine your findings into a coherent narrative.

---

## ✅ Expected Findings

```
Timeline:
03:15:01 - Failed SSH from 10.0.50.99
03:15:45 - Failed SSH from 10.0.50.99
03:16:30 - Successful SSH with svc_backup account
03:17:22 - Database query on customers.db
03:18:45 - Large data transfer (4.2GB) 

Conclusion: Attacker used compromised service account
```

---

## 🎉 Success Message

> "Outstanding investigation! You traced the attack from initial access through data exfiltration. Your timeline shows exactly what happened. This is professional-grade incident response! 🌙"

**[Badge Unlocked: Night Detective]**
