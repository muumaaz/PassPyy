#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

print("Welcome to the PyPassword Generator!")

#take input of number of characters
nr_letters= int(input("How many letters would you like in your password?\n"))
##create a string of random characters
for char in range(0, nr_letters):
  random_char = random.choice(letters)
  password += random_char
  
#take input of number of symbols
nr_symbols = int(input(f"How many symbols would you like?\n"))
##create a string of random symbols
for sym in range(0, nr_symbols):
  random_sym = random.choice(symbols)
  password += random_sym
  
#take input of number of numbers
nr_numbers = int(input(f"How many numbers would you like?\n"))
##create a string of random numbers
for num in range(0, nr_numbers):
  random_num = random.choice(numbers)
  password += random_num

#suffle password
lst = []
lst.extend(password)
random.shuffle(lst)

#print
key = ""
for char in lst:
  key += char
print(f"\nStick it to your ass, dummies: {key}")
