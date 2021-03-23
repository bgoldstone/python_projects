from tkinter import *

root = Tk()
#Text Box
e = Entry(root, width=50, borderwidth=2)

def main():
    # Disable
    # my_button = Button(root, text="Click Me!", state=DISABLED)

    # Set Size/Color
    # my_button = Button(root, text="Click Me!", padx=50, pady=50, fg="white", bg="red")
    e.pack()
    #Puts insice entry box
    e.insert(0,"Enter Your Name: ")
    my_button = Button(root, text="Enter Your Name", command=my_click)
    my_button.pack()

    root.mainloop()


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root,text=hello)
    my_label.pack()


if __name__ == '__main__':
    main()
