from tkinter import *

def hello():
    root = Tk()

    # Creating label widget
    my_label = Label(root, text="Hello, World!")

    # Puts onto screen
    my_label.pack()

    root.mainloop()

if __name__ == '__main__':
    hello()