##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################

#Factorial of a number using while loop and raise ValueError exception
def fact(number):
    number = int(number)
    if number < 0:
        raise ValueError("Negative Value")
    pickNum = 1
    i = 1
    while i <= number:
        pickNum = pickNum * i
        i = i + 1
    return pickNum

# Get user input for the number
user_input = input("Enter a number to calculate factorial value: ")
try:
    factorial_result = fact(user_input)
    print(f"{user_input}! = {factorial_result}")
except ValueError as e:
    print(f"Error: {e}")
