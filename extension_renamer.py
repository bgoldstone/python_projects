# extension_renamer.py
# a simple program to bulk rename file extensions
# Author: Ben Goldstone
import os

extension = input("Enter New File Extension: .")
for i in os.listdir():
    index = i.index(".") + 1
    if (".py" in i):
        continue
    os.rename(i, i[0:index] + extension)
