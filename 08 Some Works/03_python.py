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


print(("So I said, \"You don't know me! You'll never understand me!\""))

print(('So I said, "You don\'t know me! You\'ll never understand me!"'))

print(("This will result in only three backslashes: \\ \\ \\"))

print(("""The double quotation mark (\") is used to indicate direct quotations."""))

print("---------------------------------------------------------------------------------")
my_name = 'Akif ERSOY'
my_age = 32  # not a lie
my_height = 174
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight))
