# 🎮 Game Design Document

This document describes every mission in the Cyber Coding Game, organized by tier.

---

## 🎯 Core Design Philosophy

**"Noob to Pro"** — We take absolute beginners and gradually build them into confident defenders.

### Key Principles

1. **Start with clicks, progress to typing** — Don't ask beginners to type code immediately
2. **One concept at a time** — Never overwhelm with multiple new ideas
3. **Contextual motivation** — Every coding concept connects to a security reason
4. **Safe failure** — Mistakes give helpful feedback, never shame
5. **Visible progress** — Badges, levels, and encouragement throughout

---

## 🟢 Tier 1: New Trainee

*"You just got hired at CyberShield Corp. Welcome to the Security Operations Center! Don't worry — we'll teach you everything."*

### What This Tier Teaches
- What code is and why it matters
- Basic vocabulary (variables, strings, commands)
- What logs are and why they're important
- Foundational security awareness

### How This Tier Feels
- Hand-holding throughout
- Fill-in-the-blank before typing
- Immediate, friendly feedback
- Lots of encouragement

---

### Mission 01: Your First Line of Code 🐍

**Story:**
> Your first day at CyberShield! Your mentor, Alex, shows you the Security Operations Center. "Every cyber defender needs to know a little coding," Alex says. "Let's start with something simple."

**Coding Concept:** Variables and print()
**Security Concept:** Why automation helps defenders

**Task:**
1. First, we show working code and explain it
2. Player fills in one blank: `print("____")`
3. Player runs it and sees the output
4. Celebration! First badge earned!

**Example Interaction:**
```txt
ALEX: "Let's print a message to the screen. Type 'Hello' where the blank is!"

YOUR CODE:
print("_____")

[Type here: Hello]

[RUN BUTTON]

OUTPUT:
Hello

ALEX: "You did it! You just wrote your first line of code! 🎉"
[Badge Unlocked: Terminal Trainee]
```

**If They Make a Mistake:**
```txt
Hmm, that didn't quite work. Make sure you typed exactly "Hello".
Remember: Computers need exact spelling!
[Try Again]
```

---

### Mission 02: Meet the Terminal 🖥️

**Story:**
> "Analysts use something called a 'terminal' to type commands," Alex explains. "It looks like the movies, but it's not as scary as it seems!"

**Coding Concept:** Basic Bash commands (pwd, ls, cat)
**Security Concept:** Understanding system navigation

**Task:**
1. Type `pwd` to see where you are
2. Type `ls` to see files
3. Type `cat readme.txt` to read a file

**Example Interaction:**
```txt
ALEX: "Type 'ls' to see what files are in this folder."

trainee@cybershield:~$ ls

[Type here: ls]
[Enter]

OUTPUT:
readme.txt  welcome.txt  logs/

ALEX: "See those files? Type 'cat readme.txt' to read one!"
```

---

### Mission 03: What Are Logs? 📋

**Story:**
> Alex takes you to a screen full of scrolling text. "These are logs — they record everything that happens on our systems. Learning to read them is a superpower!"

**Coding Concept:** Simple Lucene-style queries
**Security Concept:** Introduction to log analysis

**Task:**
1. View example log entries
2. Use a simple search: `status:failed`
3. Count how many results you got

**Example Interaction:**
```txt
ALEX: "Let's find all the failed events. Type 'status:failed' in the search box."

SEARCH: status:failed

RESULTS (3 found):
[2024-01-15 09:32:15] status:failed user:john action:login
[2024-01-15 10:45:22] status:failed user:john action:login  
[2024-01-15 10:45:58] status:failed user:john action:login

ALEX: "Three failed logins from John... that might be nothing, or it might be something. 
      In real security work, you'd investigate further!"
```

---

## 🟡 Tier 2: Analyst

*"You've learned the basics. Now let's put them to work solving real (simulated) security problems!"*

### What This Tier Teaches
- Writing small scripts
- Combining commands
- Recognizing attack patterns
- Making security decisions

### How This Tier Feels
- Less hand-holding
- More typing, less clicking
- Hints available but not automatic
- Building real confidence

---

### Mission 04: Build a Log Scanner 🔍

**Story:**
> "We need a Python script that counts failed logins," your team lead says. "If someone fails more than 5 times, that's suspicious. Can you build it?"

**Coding Concept:** Python loops and conditionals
**Security Concept:** Brute force detection

**Task:**
Write a Python script that:
1. Reads through log entries
2. Counts failed logins per user
3. Flags users with more than 5 failures

**Starter Code:**
```python
# Log entries (already given to you)
logs = [
    {"user": "john", "status": "success"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "sarah", "status": "success"},
]

# Your job: Count failed logins per user
# and print if anyone has more than 5

# Hint: Start by making a variable to count
```

**Correct Solution:**
```python
failed_counts = {}

for entry in logs:
    if entry["status"] == "failed":
        user = entry["user"]
        if user in failed_counts:
            failed_counts[user] += 1
        else:
            failed_counts[user] = 1

for user, count in failed_counts.items():
    if count > 5:
        print(f"⚠️ ALERT: {user} has {count} failed logins!")
```

**Common Mistake:**
```python
# Wrong: Checking for "fail" instead of "failed"
if entry["status"] == "fail":  # ❌ Typo!
```

---

### Mission 05: Bash Pipeline Power 🔗

**Story:**
> "We've got a log file with thousands of lines. Use Bash commands to find the IPs that appear most often — they might be attackers!"

**Coding Concept:** grep, sort, uniq pipeline
**Security Concept:** IP address analysis

**Task:**
Chain Bash commands to:
1. Extract IP addresses from logs
2. Sort them
3. Count occurrences
4. Find the most frequent

**Starter:**
```bash
# The log file is at: /var/log/access.log
# Each line looks like: 192.168.1.100 - - [15/Jan/2024:09:32:15] "GET /login"

# Your job: Find which IP appears most often
# Hint: grep can extract patterns, sort arranges them, uniq -c counts
```

**Correct Solution:**
```bash
grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' /var/log/access.log | sort | uniq -c | sort -rn | head -5
```

---

### Mission 06: Advanced Log Hunting 🎯

**Story:**
> "We suspect someone is trying to access admin pages at night. Can you search for admin access between 11 PM and 5 AM?"

**Coding Concept:** Complex Lucene queries (AND, OR, ranges)
**Security Concept:** Temporal analysis

**Task:**
Write a query that finds:
- Requests to any path containing "admin"
- Between 23:00 and 05:00

**Correct Query:**
```
path:*admin* AND (hour:[23 TO 23] OR hour:[0 TO 5])
```

---

## 🔴 Tier 3: Threat Hunter

*"You're ready for the big leagues. Time to investigate realistic incidents and fix real vulnerabilities."*

### What This Tier Teaches
- Combining multiple tools
- Thinking like an investigator
- Secure coding practices
- Real-world patterns

### How This Tier Feels
- Minimal hints (high-level only)
- Open-ended problems
- Multiple valid approaches
- Professional confidence

---

### Mission 07: The Midnight Breach 🌙

**Story:**
> "ALERT: Our monitoring system flagged unusual activity at 3:17 AM last night. Someone accessed the database server. We need to know: Who? How? What did they touch?"

**Coding Concept:** Multi-tool investigation
**Security Concept:** Incident response basics

**Task:**
Use all your skills to:
1. Find the suspicious connection in logs
2. Trace what the attacker did
3. Determine what data was accessed
4. Write a brief incident report

**Available Tools:**
- Python script to parse logs
- Bash commands on simulated server
- Lucene search on log database

---

### Mission 08: Fix the Vulnerable Code 🔧

**Story:**
> "Our security scanner found a vulnerability in our user registration code. Can you spot the problem and fix it?"

**Coding Concept:** Input validation
**Security Concept:** Injection prevention

**Vulnerable Code:**
```python
def create_user(username, email):
    # This code is INSECURE! Can you spot why?
    query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
    database.execute(query)
    return "User created!"
```

**Fixed Code:**
```python
def create_user(username, email):
    # Fixed: Using parameterized queries
    query = "INSERT INTO users (username, email) VALUES (?, ?)"
    database.execute(query, (username, email))
    return "User created!"
```

---

### Mission 09: Build a Brute Force Detector 🛡️

**Story:**
> "We need a more sophisticated detector. Build a Python script that can identify brute force attacks with multiple patterns."

**Coding Concept:** Algorithm design
**Security Concept:** Attack pattern recognition

**Requirements:**
- Detect more than 5 failures in 1 minute (fast attack)
- Detect more than 10 failures in 10 minutes (slow attack)
- Flag username enumeration (many users, same password pattern)

---

### Mission 10: Final Challenge - Full Investigation 🏆

**Story:**
> "Welcome to your final test, Threat Hunter. Last weekend, we detected anomalous activity that set off multiple alerts. We need a complete investigation, analysis, and recommendation."

**Task:**
Complete a realistic incident investigation using everything you've learned:
1. Analyze multiple log sources
2. Build a timeline of the attack
3. Identify the attack vector
4. Write a professional incident report
5. Recommend security improvements

**Upon Completion:**
```
🎉 CONGRATULATIONS! 🎉

You've completed the Cyber Coding Game!

From "What is code?" to full incident investigations,
you've grown into a true Cyber Defender.

[Badge Unlocked: Threat Hunter Elite 🛡️]

Remember: Use your skills to PROTECT, never to harm.
The digital world needs defenders like you!
```

---

## 🏅 Badges & Rewards

| Badge | Earned When |
|-------|-------------|
| 🌱 Terminal Trainee | Complete Mission 01 |
| 🖥️ Command Liner | Complete Mission 02 |
| 📋 Log Reader | Complete Mission 03 |
| 🔍 Pattern Finder | Complete Mission 04 |
| 🔗 Pipeline Pro | Complete Mission 05 |
| 🎯 Search Expert | Complete Mission 06 |
| 🌙 Night Detective | Complete Mission 07 |
| 🔧 Code Fixer | Complete Mission 08 |
| 🛡️ Attack Detector | Complete Mission 09 |
| 🏆 Threat Hunter Elite | Complete Mission 10 |

---

## ⚙️ Difficulty Settings

Players can adjust difficulty at any time:

| Setting | Effect |
|---------|--------|
| 🐢 Relaxed | More hints, simpler challenges, no time pressure |
| ⚖️ Standard | Balanced experience (recommended) |
| 🚀 Challenge | Fewer hints, bonus objectives, harder variants |

---

## 📐 Mission Template

For contributors adding new missions:

```markdown
### Mission XX: [Title] [Emoji]

**Story:** [1-3 sentences setting the scene]
**Coding Concept:** [One specific skill]
**Security Concept:** [One specific awareness point]

**Task:** [What the player needs to do]
**Starter Code:** [If applicable]
**Correct Solution:** [One working answer]
**Common Mistake:** [What beginners often do wrong and why]
```
