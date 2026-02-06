# Mission 01: Your First Line of Code 🐍

**Tier:** 🟢 New Trainee  
**Language:** Python  
**XP Reward:** 10  
**Badge:** Terminal Trainee

---

## 📖 Story Setup

> Welcome to CyberShield Corp, recruit!
>
> I'm Alex, your mentor in the Security Operations Center. Don't worry if you've never coded before — everyone starts somewhere, and I'll be right here to help.
>
> "Every cyber defender needs to know a little coding," Alex says with a smile. "Let's start with something super simple. We're going to make the computer say 'Hello, World!' — it's a tradition for every coder's first program."

---

## 🎯 Learning Goals

### Coding Concept: print() Function

The `print()` function displays text on the screen. Whatever you put inside the parentheses (in quotes) will appear as output.

```python
print("This text will appear on screen!")
```

### Security Concept: Why Automation Helps Defenders

Cyber defenders write code to automate tasks. Instead of manually checking thousands of logs, a script can do it in seconds. This first step — learning to write code — is the beginning of becoming a powerful defender.

---

## 📋 Your Task

Make the computer display `Hello, World!` on the screen.

### Step 1: Understand the syntax

```python
print("message here")
```

- `print` is the command
- `()` wraps what you want to print
- `""` wraps your text message

### Step 2: Type your code

```python
print("Hello, World!")
```

### Step 3: Run it

Click the "Run Code" button and watch your message appear.

---

## ✅ Correct Solution

```python
print("Hello, World!")
```

**Output:**

```
Hello, World!
```

---

## ❌ Common Mistakes

### Mistake 1: Forgetting quotes

```python
print(Hello, World!)  # ❌ Missing quotes
```

**Error:** `NameError: name 'Hello' is not defined`
**Why:** Python thinks Hello is a variable name, not text. Use quotes!

### Mistake 2: Wrong brackets

```python
print["Hello, World!"]  # ❌ Square brackets
```

**Error:** `TypeError`
**Why:** Functions use parentheses `()`, not square brackets `[]`

### Mistake 3: Missing parentheses

```python
print "Hello, World!"  # ❌ No parentheses
```

**Error:** `SyntaxError`
**Why:** In Python 3, print requires parentheses

---

## 💡 Hints

1. Start with the word `print`
2. Add parentheses after it: `print()`
3. Put your message inside quotes: `print("Hello, World!")`
4. Make sure to match your quote marks (both single or both double)

---

## 🎉 Success Message

> "You did it! You just wrote your first line of code! The `print()` function is one of the most useful tools — you'll use it constantly to see what your programs are doing. Welcome to the world of coding, defender! 🛡️"

**[Badge Unlocked: Terminal Trainee]**
