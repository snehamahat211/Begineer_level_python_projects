import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password Generator")
nr_letters=int(input("Enter the number of letters"))
nr_symbol=int(input("Enter the number of  symbol"))
nr_number=int(input("Enter the number of numbers"))
password=""

for position in range(1,nr_letters+1):
    password+=random.choice(letters)



for position in range(1,nr_symbol+1):
    password+=random.choice(symbols)




for position in range(1,nr_number+1):
    password+=random.choice(numbers)

print(password)
