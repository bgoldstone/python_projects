# remove_public_shortcuts.py
# Removes all public desktop shortcuts
import os

if __name__ == "__main__":
    try:
        for file in os.listdir(r'C:\Users\Public\Desktop'):
            if file.endswith('.lnk'):
                print("\n" + file, end="")
                os.remove(file)
    except FileNotFoundError:
        print(" not found", end="")
