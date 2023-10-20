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


while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if not user_input:
        break

    try:
        number = int(user_input)
        result = number ** 2
        print(f"The square of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Exiting the program.")
