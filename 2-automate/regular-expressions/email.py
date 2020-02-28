"""A simple program to check strength of a password"""


import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):
    if (re.search(regex,email)):
        print("Valid Email")

    else:
        print("Invalid Email")

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         get_password_strength(sys.argv[1])
#     else:
#         is_pass_strong = False
#         while not is_pass_strong:
#             password = input('Enter Password: ')
#             is_pass_strong = get_password_strength(password)
