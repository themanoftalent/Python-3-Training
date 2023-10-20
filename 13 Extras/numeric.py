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

print("Enter a number between 1 and 100:")
x = input()

try:
    x = int(x)
    if x > 100:
        print("That number is too big!")
    elif x < 1:
        print("That number is too small!")
    else:
        print("{} is a good number.".format(x))
except ValueError:
    print("Invalid input. Please enter a valid number.")

