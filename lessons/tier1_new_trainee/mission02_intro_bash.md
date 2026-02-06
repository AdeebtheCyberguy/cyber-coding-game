# Mission 02: Meet the Terminal 🖥️

**Tier:** 🟢 New Trainee  
**Language:** Bash  
**XP Reward:** 10  
**Badge:** Command Liner

---

## 📖 Story Setup

> Alex leads you to a computer with a black screen and a blinking cursor.
>
> "This is a terminal," Alex explains. "It might look like something from a hacker movie, but it's really just a way to talk directly to the computer by typing commands."
>
> "Think of it like texting the computer. You type a command, press Enter, and it responds. Let's learn the basics!"

---

## 🎯 Learning Goals

### Coding Concept: Basic Bash Commands

The terminal accepts commands that tell the computer what to do:

| Command | What it does |
|---------|-------------|
| `pwd` | Print Working Directory — shows where you are |
| `ls` | List — shows files in current folder |
| `cat` | Concatenate — displays file contents |

### Security Concept: System Navigation

Security analysts need to navigate systems to investigate incidents. Knowing how to move around and view files is fundamental to any investigation.

---

## 📋 Your Task

### Part 1: Where am I?

Type `pwd` to see your current location:

```bash
pwd
```

**Expected output:** `/home/trainee`

### Part 2: What files are here?

Type `ls` to see files in this folder:

```bash
ls
```

**Expected output:** `readme.txt  welcome.txt  logs/`

### Part 3: Read a file

Type `cat readme.txt` to read the contents:

```bash
cat readme.txt
```

---

## ✅ Correct Solution

```bash
# See where you are
pwd

# List files
ls

# Read a file
cat readme.txt
```

---

## ❌ Common Mistakes

### Mistake 1: Typing with capitals

```bash
PWD  # ❌ Commands are case-sensitive!
```

**Why:** Linux commands are lowercase. `pwd` works, `PWD` doesn't.

### Mistake 2: Forgetting the filename

```bash
cat  # ❌ Cat what?
```

**Error:** `cat: missing operand`
**Why:** You need to tell `cat` which file to read.

### Mistake 3: Wrong filename

```bash
cat readmee.txt  # ❌ Typo in filename
```

**Error:** `No such file or directory`
**Why:** Filenames must be exact. Use `ls` to see correct names.

---

## 💡 Hints

1. Commands are typed in lowercase
2. Press Enter after each command
3. Use `ls` to see what files exist before trying to read them
4. Filenames are case-sensitive (`readme.txt` ≠ `Readme.txt`)

---

## 🎉 Success Message

> "Nice work! You just learned to navigate the terminal like a pro. These commands — `pwd`, `ls`, and `cat` — are the foundation of everything you'll do as a security analyst. You're already speaking the computer's language! 🖥️"

**[Badge Unlocked: Command Liner]**
