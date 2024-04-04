# Task 2: Password Generator

# First we will use the random Module of pyhton to help in selecting random variable for password generation.
import random

length=int(input("Enter the length of the password:\n[IMP Length >5]\n"))
chars="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+/*-+"
password=""
for x in range(0,length):
    password=password+random.choice(chars)
print(password)
    
