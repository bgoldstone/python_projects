# Learning regular expression through automate the boring stuff with python
import re  # import regular expressions
if __name__ == '__main__':
    # compiles expression
    phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # searches for matching expression
    test_phone_number = phone_num_regex.search(input("Enter a phone number "))
    print("Phone number found:", test_phone_number.group())
