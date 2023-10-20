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

def string_operations(input_string):
    print("Original String:", input_string)
    print("Capitalized:", input_string.capitalize())
    print("Title Case:", input_string.title())
    print("Uppercase:", input_string.upper())
    print("Swapped Case:", input_string.swapcase())
    print("Find 'is':", input_string.find('is'))
    print("Replace 'this' with 'that':", input_string.replace('this', 'that'))
    print("Stripped of leading and trailing spaces:", input_string.strip())
    print("Is Alphanumeric:", input_string.isalnum())
    print("Is Alphabetical:", input_string.isalpha())
    print("Is Numeric:", input_string.isdigit())
    print("Is Printable:", input_string.isprintable())

def main():
    s = 'this is a string'
    string_operations(s)

if __name__ == "__main__":
    main()
