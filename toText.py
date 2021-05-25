#!/bin/python3

'''
A file that converts ASCII to text
'''

def main():
    ascii_to_convert = '72 101 108 108 111 44 32 87 111 114 108 100'
    converted_str = ""
    for i in ascii_to_convert.split(' '):
        converted_str += chr(int(i))
    print(converted_str)
if __name__ == '__main__':
    main()