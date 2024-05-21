import random

# Define lists of characters to choose from
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
    '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
    '{', '|', '}', '~'
]
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Get the number of each type of character from the user
nr_alphabets = int(input("How many alphabets you want to see in your password:\n"))
nr_numbers = int(input("How many numbers you want to see in your password:\n"))
nr_symbols = int(input("How many symbols you want to see in your password:\n"))

# Initialize an empty password string
password = ""

# Add random alphabets to the password
for char in range(1, nr_alphabets + 1):
    password += random.choice(alphabets)

# Add random digits to the password
for char in range(1, nr_numbers + 1):
    password += random.choice(digits)

# Add random symbols to the password
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# Convert the password string to a list and shuffle it to randomize the order
password = list(password)
random.shuffle(password)
password = "".join(password)  # Convert the list back to a string

# Print the final password
print("Your Password is Here:", password)
