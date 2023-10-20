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



# Create a rectangle pattern
print("#" * 15)  # Top border
for _ in range(7):
    print("#" + " " * 13 + "#")  # Middle part with spaces
print("#" * 15)  # Bottom border

print("")  # Add a blank line

# Create a staircase pattern
for i in range(10):
    print("#" * (i + 1))

