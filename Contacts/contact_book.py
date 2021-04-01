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

    while (choice != 'Q'):
        print("What would you like to do? ")
        print("(V)iew a Contact")
        print("(A)dd a Contact")
        print("(R)emove a Contact")
        print("(Q)uit")
        choice = input("Please select an Option: ").upper()[0]
        if (choice == 'V'):
            view(input("Enter the Name you would like to search for "))
        if (choice == 'A'):
            add()


def view(name):
    i = True
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
    contact = []
    contact_file = open('contacts.csv', 'a+')
    for field in fields:
        contact_file.write(input(f"Enter the contact's {field} ") + ',')
    contact_file.write("\n")
    contact_file.close()


def remove():
    pass


if __name__ == '__main__':
    main()
