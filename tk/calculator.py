from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=35, borderwidth=5)
global f_num, math
f_num = 0
math = ""

def main():
    # Disable
    # my_button = Button(root, text="Click Me!", state=DISABLED)

    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # define buttons
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
    button_add = Button(root, text="+", padx=39, pady=20, command=add_numbers)
    button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract_numbers)
    button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply_numbers)
    button_divide = Button(root, text="/", padx=41, pady=20, command=divide_numbers)
    button_equal = Button(root, text="=", padx=87, pady=20, command=equals)
    button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear_input)
    # Puts buttons on screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)

    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)
    root.mainloop()


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear_input():
    e.delete(0, END)
    global f_num
    f_num = 0


def add_numbers():
    global f_num
    global math
    math = "addition"
    f_num += int(e.get())
    e.delete(0, END)


def subtract_numbers():
    global f_num
    global math
    math = "subtraction"
    if f_num != 0:
        f_num -= int(e.get())
    else:
        f_num = int(e.get())
    e.delete(0, END)


def multiply_numbers():
    global f_num
    global math
    math = "multiplication"
    if f_num != 0:
        f_num *= int(e.get())
    else:
        f_num = int(e.get())
    e.delete(0, END)


def divide_numbers():
    global f_num
    global math
    math = "division"
    if f_num != 0:
        f_num /= int(e.get())
    else:
        f_num = int(e.get())
    e.delete(0, END)


def equals():
    if math == "addition":
        s_num = int(e.get())
        e.delete(0, END)
        e.insert(0, f_num + s_num)

    elif math == "subtraction":
        s_num = int(e.get())
        e.delete(0, END)
        e.insert(0, f_num - s_num)

    elif math == "multiplication":
        s_num = int(e.get())
        e.delete(0, END)
        e.insert(0, f_num * s_num)

    elif math == "division":
        s_num = int(e.get())
        e.delete(0, END)
        e.insert(0, f_num / s_num)


if __name__ == '__main__':
    main()
