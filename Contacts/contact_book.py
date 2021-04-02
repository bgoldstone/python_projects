# contact_book.py
# Simple not efficient contact book
import os


def main():
    global fields, writer, reader
    fields = ['Name', 'Address', 'City', 'State/Province', 'Zip/Postal Code', 'Home Phone', 'Mobile Phone',
              'Email Address']
    choice = ' '
    if ('contacts.csv' not in os.listdir()):
        contact_file = open('contacts.csv', 'w+')
        for field in fields:
            contact_file.write(field)
            contact_file.write(',')
        contact_file.write('\n')
        contact_file.close()
    contact_file = open('contacts.csv', 'w+')
    if (contact_file.readline() == ''):
        for field in fields:
            contact_file.write(field)
            contact_file.write(',')
        contact_file.write('\n')
        contact_file.close()
    while (choice != 'Q'):
        print("What would you like to do? ")
        print("(V)iew a Contact")
        print("(A)dd a Contact")
        print("(R)emove a Contact")
        print("(Q)uit")
        choice = input("Please select an Option: ").upper()[0]
        if (choice == 'V'):
            view(input("Enter the name you would like to search for "))
        if (choice == 'A'):
            add()
        if (choice == 'R'):
            remove(input("Enter the name you want to remove "))


def view(name):
    with open('contacts.csv', 'r') as contact_file:
        for index, lines in enumerate(contact_file):
            if index == 0:
                continue
            else:
                line = lines.split(',')
                if (line[0] == name):
                    print("Contact:")
                    for i, field in enumerate(fields):
                        print(f"    {field}: {line[i]}")
                    print("\n\n")


def add():
    contact_file = open('contacts.csv', 'a+')
    for field in fields:
        contact_file.write(input(f"Enter the contact's {field} ") + ',')
    contact_file.write("\n")
    contact_file.close()


def remove(name):
    with open('contacts.csv', 'r') as reader:
        with open('contacts_tmp.csv', 'w') as writer:
            for line in reader:
                if (line.split(',')[0] != name):
                    writer.write(line)
    os.replace('contacts_tmp.csv', 'contacts.csv')


if __name__ == '__main__':
    main()
