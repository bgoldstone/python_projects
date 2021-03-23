from tkinter import *

root = Tk()


def main():
    # Disable
    # my_button = Button(root, text="Click Me!", state=DISABLED)

    # Set Size
    # my_button = Button(root, text="Click Me!", padx=50, pady=50)
    my_button = Button(root, text="Click Me!", command=my_click, fg="white",bg="red")
    my_button.pack()

    root.mainloop()


def my_click():
    my_label = Label(root, text="Look! I clicked a Button!!")
    my_label.pack()


if __name__ == '__main__':
    main()
