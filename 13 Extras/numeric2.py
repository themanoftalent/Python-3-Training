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

print("Enter a number between 7 and 72:")
y = input()

try:
    y = int(y)
    if 7 <= y <= 72:
        print("{} is a good number.".format(y))
    elif y > 72:
        print("That number is too big!")
    else:
        print("That number is too small!")
except ValueError:
    print("Invalid input. Please enter a valid number.")

