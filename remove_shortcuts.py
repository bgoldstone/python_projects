# remove_shortcuts.py
# Removes all desktop shortcuts
import os

if __name__ == "__main__":
    os.chdir(os.path.expanduser('~') + r'\Desktop')
    for file in os.listdir():
        if file.endswith('.lnk'):
            print(file)
            os.remove(file)
