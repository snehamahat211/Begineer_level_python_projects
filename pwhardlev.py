import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to the password generator game")
nr_letters=int(input("Enter the number of letters \n"))
nr_symbols=int(input("Enter the number of symbols\n"))
nr_numbers=int(input("Enter the number of numbers\n"))
password_list=[]
for position in range(1,nr_letters+1):
    password_list+=random.choice(letters)
for position in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)
for position in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in  password_list:
    password+=char
print(f"your password is {password}")



