# Mission 05: Bash Pipeline Power 🔗

**Tier:** 🟡 Analyst  
**Language:** Bash  
**XP Reward:** 25  
**Badge:** Pipeline Pro

---

## 📖 Story Setup

> A massive log file just landed on your desk — thousands of lines.
>
> "We need to know which IP addresses appear most often," your lead explains. "The most frequent IPs might be attackers. Use Bash pipelines to analyze this."

---

## 🎯 Learning Goals

### Coding Concept: Command Pipelines

The pipe symbol `|` connects commands. Output from one becomes input to the next.

| Command | Purpose |
|---------|---------|
| `grep PATTERN file` | Find lines matching pattern |
| `sort` | Arrange lines alphabetically |
| `uniq -c` | Count repeated lines (needs sorted input) |
| `head -n N` | Show first N lines |

### Security Concept: IP Address Analysis

Attackers often come from specific IPs. Finding which IPs appear most helps identify potential threats.

---

## 📋 Your Task

Chain together Bash commands to:

1. Extract all IP addresses from the log
2. Sort them
3. Count occurrences
4. Show the top 5 most frequent

---

## ✅ Correct Solution

```bash
grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' /var/log/access.log | sort | uniq -c | sort -rn | head -5
```

**Output:**

```
      5 10.0.50.99
      3 192.168.1.100
      1 192.168.1.101
```

**Analysis:** IP 10.0.50.99 appears most — definitely worth investigating!

---

## 💡 Hints

1. Use `grep` to find patterns
2. Pipe output with `|`
3. `uniq` requires sorted input to work correctly
4. `sort -rn` sorts numerically in reverse (highest first)

---

## 🎉 Success Message

> "Pipeline master! You just processed thousands of log lines in one command. That suspicious IP 10.0.50.99? It's showing up everywhere. Time to investigate! 🔗"

**[Badge Unlocked: Pipeline Pro]**
