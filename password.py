import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
           "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*",
           "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", '"', ",", ".", "<", ">", "/", "?", "~", "`"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the simple password generator.")
n_letters = int(input("How many letters you want in your password\n"))
n_symbols = int(input("How many symbols you want in your password\n"))
n_numbers = int(input("How many numbers you want in your password\n"))

password = ""
for i in range(n_letters):
    password += random.choice(letters)

for i in range(n_symbols):
    password += random.choice(symbols)

for i in range(n_numbers):
    password += random.choice(numbers)

password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)

print(final_password)
