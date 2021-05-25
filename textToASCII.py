#!/bin/python3

'''
A file to convert text to ASCII
'''


def main():
    str_to_convert = 'Hello, World'
    unicode = ''
    for i in str_to_convert:
        unicode += str(ord(i))
        unicode += ' '
    print(unicode)


if __name__ == '__main__':
    main()
