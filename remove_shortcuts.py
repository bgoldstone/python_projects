# remove_shortcuts.py
# Removes all desktop shortcuts
import os

if __name__ == "__main__":
    try:
        for file in os.listdir(os.path.expanduser('~') + r'\Desktop'):
            if file.endswith('.lnk'):
                print("\n" + file, end="")
                os.remove(file)
    except FileNotFoundError:
        print(" not found", end="")
