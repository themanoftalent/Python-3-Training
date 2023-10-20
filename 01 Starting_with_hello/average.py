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

# Write a program that asks the user for 5 numbers and then prints the average of these numbers.
# Initialize a variable to store the sum of the numbers
total = 0

# Get 5 numbers from the user
for i in range(5):
    try:
        # Ask the user for input and convert it to a float
        num = float(input(f"Enter number {i + 1}: "))

        # Add the number to the total
        total += num
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the average
average = total / 5

# Print the average
print(f"The average of the 5 numbers is: {average}")
