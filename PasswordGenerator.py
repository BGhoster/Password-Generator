"""
Generates a random password based on user inputs
Checks the length of password
Verifies password meets requirements
"""

import string
import random
import re

def generate_random_password(password_letters, password_symbols, password_numbers):
    """
    Generates a random password using letters, symbols, and numbers.
    """

    # Sets up characters for password
    ascii_letters = string.ascii_letters
    ascii_numbers = string.digits
    ascii_symbols = string.punctuation
    
    # Generates a password based on user inputs
    password_letters = ''.join(random.choice(ascii_letters) for i in range(password_letters))
    password_numbers = ''.join(random.choice(ascii_numbers) for i in range(password_numbers))
    password_symbols = ''.join(random.choice(ascii_symbols) for i in range(password_symbols))
   
   # Randomly shuffles password characters
    password_list = list(password_letters + password_numbers + password_symbols)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def validate_password(password):
    """
    Validates if the password meets the requirements and returns it if it does.
    """
    # Verifies password meets minimum password
    has_three_letters = len(re.findall(r'[a-zA-Z]', password)) >= 3
    has_number = len(re.findall(r'\d', password)) >= 1
    has_symbol = len(re.findall(r'[\W_]', password)) >= 1
    
    # Does a simple check on password
    if has_three_letters and has_number and has_symbol and len(password) >= 7:
        print(f"Password is {password}")
    else:
        print("Requirements are not met")
        create_password()

    return password

def create_password():
    while True:
        try:
            print("Create a password with 3 letters, 1 number, and 1 symbol")
            user_letters = int(input("Enter the amount of letters: "))
            user_numbers = int(input("Enter the amount of numbers: "))
            user_symbols = int(input("Enter the amount of symbols: "))

            validate_password(generate_random_password(user_letters, user_numbers, user_symbols))
            break
        
        except ValueError:
            print("Please enter a number")

        except Exception as e:
            print(e)

create_password()
