import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
letter_input = int(input("How many letters do you want in your password? "))
number_input = int(input("How many numbers do you want in your password? "))
symbol_input = int(input("How many symbols do you want in your password? "))
password = []
for letter in range(letter_input):
    password += random.choice(letters)

for number  in range(number_input):
     password += random.choice(numbers)
for symbol in range(symbol_input):
     password += random.choice(symbols)
random.shuffle(password)
print(password)
hard_password = ""
for char in password:
     hard_password += char
print(hard_password)
