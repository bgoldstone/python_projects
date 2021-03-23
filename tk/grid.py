from tkinter import *

def main():
    root = Tk()

    # Creating label widgets
    my_label1 = Label(root, text="Hello, World!")
    my_label2 = Label(root, text="My Name is Ben Goldstone")
    my_label3 = Label(root, text=" ")

    # Puts onto screen
    my_label1.grid(row=0, column=0)
    my_label2.grid(row=1,column=0)
    my_label3.grid(row=2,column=0)

    root.mainloop()

if __name__ == '__main__':
    main()