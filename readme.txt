This repository contains a Python script that generates a random password based on user inputs and validates if the password meets the requirements.

The generate_random_password function takes in three parameters - password_letters, password_symbols, and password_numbers - which represent the number of letters, symbols, and numbers in the password respectively. The function generates a random password using the string and random libraries and returns the password as a string.

The validate_password function takes in a password as a parameter and validates if the password meets the requirements. The password must contain at least 3 letters, 1 number, and 1 symbol, and be at least 8 characters long. If the password meets these requirements, the function returns the password. Otherwise, it prompts the user to create a new password that meets the requirements.

The create_password function prompts the user to input the number of letters, symbols, and numbers they want in the password, and then generates a random password using the generate_random_password function. It then validates the password using the validate_password function, and prompts the user to create a new password if the password does not meet the requirements.

To run the script, simply run the create_password() function.