# RemoveDesktopShortcuts.py
# Removes all desktop shortcuts
import os

if __name__ == "__main__":
    os.chdir(os.path.expanduser('~') + r'\Desktop')
    for i in os.listdir():
        if i.endswith('.lnk'):
            print(i)
            os.remove(i)
