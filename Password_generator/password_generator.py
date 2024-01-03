import random
import string 

def password_generator(length):
    custom_characters = '!#$%&/=*+@-~?'
    characters = string.ascii_letters + string.digits + custom_characters

    exclude_chars_option = input("Do you want to exclude specific characters? (yes/no): ").lower()

    if exclude_chars_option == "yes":
        print('Custom characters: ! # $ % & / = * + @ - ~ ?')
        exclude_chars_input = input('Enter the characters you want to exclude: ' )
        characters = ''.join(char for char in characters if char not in exclude_chars_input) 
    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

desired_length = int(input("Enter the desired password length: "))
    
resulting_password = password_generator(desired_length)
print("Generated Password:", resulting_password)
