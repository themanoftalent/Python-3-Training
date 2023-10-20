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

class Dog:
    # Class constructor (initialize the object)
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    # Method to make the dog bark
    def bark(self):
        return f"{self.name} is barking."

    # Method to teach the dog a new trick
    def teach_trick(self, trick):
        self.tricks.append(trick)
        return f"{self.name} has learned a new trick: {trick}"

    # Method to display information about the dog
    def display_info(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nTricks: {', '.join(self.tricks)}"

# Create instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Teach some tricks to the dogs
dog1.teach_trick("Sit")
dog1.teach_trick("Roll Over")
dog2.teach_trick("Fetch")

# Display information about the dogs
print("Dog 1 Info:")
print(dog1.display_info())

print("\nDog 2 Info:")
print(dog2.display_info())
