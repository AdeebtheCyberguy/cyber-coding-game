# Mission 03: What Are Logs? 📋

**Tier:** 🟢 New Trainee  
**Language:** Lucene Search  
**XP Reward:** 15  
**Badge:** Log Reader

---

## 📖 Story Setup

> Alex points to a screen filled with scrolling text.
>
> "These are logs," Alex explains. "Every time something happens on our systems — someone logs in, accesses a file, or tries something suspicious — it gets recorded here."
>
> "There's a lot of information, right? That's where searching comes in. Learning to find the important stuff in all this noise is like having a superpower."

---

## 🎯 Learning Goals

### Coding Concept: Log Search Queries

We use search queries to find specific information:

```
field:value
```

Examples:

- `status:failed` — Find all failed events
- `user:john` — Find all events for user John
- `ip:10.0.50.99` — Find all events from this IP

### Security Concept: Log Analysis

Logs tell the story of what happened on a system. Security analysts read logs to detect attacks, investigate incidents, and understand threats.

---

## 📋 Your Task

### Part 1: Explore the logs

Look at the log entries in the viewer. Notice the patterns:

```
timestamp | level | user | action | status | ip
```

### Part 2: Find failed logins

Type this search query:

```
status:failed
```

### Part 3: Analyze results

How many failed login attempts do you see? Notice anything interesting?

---

## ✅ Correct Solution

```
status:failed
```

**Results found:** 5 entries

**Analysis:**

- All failed logins are for user `john`
- They all come from IP `10.0.50.99`
- They happened within seconds of each other

This pattern suggests someone was trying to guess John's password!

---

## ❌ Common Mistakes

### Mistake 1: Using the wrong field

```
failed:status  # ❌ Field and value swapped
```

**Why:** Format is `field:value`, not `value:field`

### Mistake 2: Adding spaces

```
status: failed  # ❌ Space after colon
```

**Why:** No space between field, colon, and value

### Mistake 3: Searching for partial match without wildcard

```
status:fail  # ❌ Partial word without *
```

**Why:** Use `status:fail*` for partial matches

---

## 💡 Hints

1. Format is always `field:value`
2. No spaces around the colon
3. Common fields: status, user, action, ip
4. Common values: success, failed, login, logout

---

## 🎉 Success Message

> "You found them! Those 5 rapid-fire failed logins from the same IP address? That's a classic sign of a brute force attack — someone trying to guess a password. In the real world, this is exactly the kind of pattern a security analyst would investigate. You're already thinking like a defender! 📋"

**[Badge Unlocked: Log Reader]**
