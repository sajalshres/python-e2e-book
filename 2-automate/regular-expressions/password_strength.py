"""A simple program to check strength of a password"""

import sys
import re

def get_password_strength(password):
    """Check strength of a given password

    Parameters:
    password (string): Password to check strength

    Returns:
    boolean
    """
    # Password strength regular expressions
    # At least 8 characters
    char_regex = re.compile(r'(\w{8,})')
    # At least 1 lowercase letter
    lower_regex = re.compile(r'[a-z]+')
    # At least 1 uppercase letter
    upper_regex = re.compile(r'[A-Z]+')
    # At least 1 digit
    digit_regex = re.compile(r'[0-9]+')
    # At least 1 special character
    special_regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]+')
    # No whitespace
    whitespace_regex = re.compile(r'^\s-')

    if char_regex.findall(password) == []:
        print('Password must include atleast 8 characters')
        return False
    elif lower_regex.findall(password) == []:
        print('Password must include atleast 1 lower case letter')
        return False
    elif upper_regex.findall(password) == []:
        print('Password must include atleast 1 upper case letter')
        return False
    elif digit_regex.findall(password) == []:
        print('Password must include atleast 1 digit')
        return False
    elif special_regex.findall(password) == []:
        print('Password must include atleast 1 special character')
        return False
    elif whitespace_regex.findall(password) == []:
        print('Password must not include white space')
        return False
    else:
        print('Your passowrd is strong, awesome!')
        return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_password_strength(sys.argv[1])
    else:
        is_pass_strong = False
        while not is_pass_strong:
            password = input('Enter Password: ')
            is_pass_strong = get_password_strength(password)
