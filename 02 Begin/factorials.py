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

def factorialz(number):

    if number == 0:
        return 1
    return number * factorialz(number - 1)


print(factorialz(5))

#print("Another  method")
'''
import math
math.factorial(n)
'''
