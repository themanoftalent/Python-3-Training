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



# Write a program that takes your full name as input and displays the abbreviations of the first and middle names except
# the last name which is displayed as it is.


name = input("Enter your full name here: ")

# Split the full name into words
words = name.split()

# Initialize a variable to store the initials
initials = ''

# Iterate through the words and extract the first character of each
for word in words:
    initials += word[0] + '. '

# Print the initials
print(initials)
