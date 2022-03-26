#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letters_password = ''
# for n in range(1, nr_letters + 1):
#   random_letter_order = random.randint(0,len(letters)-1)
#   letters_password += letters[random_letter_order]    

# symbols_password = ''
# for n in range(1, nr_symbols + 1):
#   random_symbol_order = random.randint(0,len(symbols)-1)
#   symbols_password += symbols[random_symbol_order]      

# numbers_password = ''
# for n in range(1, nr_numbers + 1):
#   random_number_order = random.randint(0,len(numbers)-1)
#   numbers_password += numbers[random_number_order]    

# easy_password = letters_password+symbols_password+numbers_password
# print("easy password")
# print(easy_password)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# hard_password = ''.join(random.sample(easy_password,len(easy_password)))
# print("hard password")
# print(hard_password)


## Angela Yu Answer
# Eazy Level
# password = ""
# nr_letters = 4
# for char in range(1, nr_letters + 1):
#     password  += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password  += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password  += random.choice(numbers)
# #will append to password variable by the loop order


#  Hard Level
password_list = []

for char in range(1, nr_letters + 1):
    password_list  += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_list  += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list  += random.choice(numbers)

# shuffle in list
print(password_list)
random.shuffle(password_list)
print(password_list)

# using for loop to change back list to character
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")