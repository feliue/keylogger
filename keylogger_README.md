# ⌨️ Educational Keylogger

A simple Python keylogger built for cybersecurity learning — records keystrokes, saves them to a log file, and teaches you how attackers capture keyboard input so you can defend against it.

---

## 📌 Features

- ✅ Records every key pressed
- ✅ Saves all keys to a log file
- ✅ Shows live key display on screen
- ✅ Detects special keys (Space, Enter, Backspace etc.)
- ✅ Stops automatically after set number of keys
- ✅ Press ESC anytime to stop
- ✅ Shows full summary when done
- ✅ Simple, clean, easy to understand code

---

## 🚀 How to Run

**Step 1 — Install the library:**
```bash
pip install pynput
```

**Step 2 — Run the keylogger:**
```bash
python keylogger.py
```

**Step 3 — Stop it:**
- Press **ESC** to stop
- Or close the terminal

---

## 🖥️ Demo

```
=====================================
   EDUCATIONAL KEYLOGGER
   Author: Abdulhakeem Umar Toyin
=====================================

  Log file   : keylog.txt
  Key limit  : 200
  Started at : 2025-01-01 14:30:00

  Listening for keys... (Press ESC to stop)

  Key pressed: H
  Key pressed: e
  Key pressed: l
  Key pressed: l
  Key pressed: o
  Key pressed: [SPACE]
  Key pressed: [ENTER]
  Line typed : Hello

  SUMMARY
  Total keys captured : 6
  Log saved to        : keylog.txt
```

---

## 📁 Project Structure

```
keylogger/
│
├── keylogger.py    # Main keylogger script
├── keylog.txt      # Generated log file (created when you run it)
└── README.md       # Documentation
```

---

## 📚 What I Learned

- How keyloggers work under the hood
- Python `pynput` library for keyboard monitoring
- Event-driven programming (on_press, on_release)
- File handling in Python (reading and writing)
- Why endpoint security tools detect keyloggers
- How to defend against malicious keyloggers

---

## 🛡️ How to Defend Against Keyloggers

| Defence | How it helps |
|---------|-------------|
| Antivirus software | Detects known keyloggers |
| Virtual keyboard | Bypasses keystroke capture |
| 2FA authentication | Even if password stolen, account stays safe |
| Regular OS updates | Patches vulnerabilities |
| Check running processes | Spot unknown programs |

---

## ⚠️ Legal Disclaimer

> **Only run this on your OWN computer.**
> Installing a keylogger on someone else's device
> without their permission is **ILLEGAL** in most countries
> and can result in criminal prosecution.
> This tool is for **educational purposes only** — to understand
> how keyloggers work so you can defend against them.

---

## 📜 License

MIT License — free to use and modify.

---

## 👤 Author

**Abdulhakeem Umar Toyin**
Cybersecurity Student
GitHub: [@feliue](https://github.com/feliue)
Email: abdulhakeemumar616@gmail.com
