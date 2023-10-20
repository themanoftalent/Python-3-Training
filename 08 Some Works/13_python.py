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



def allowed_dating_age(my_age):
    girls_age = (my_age/2)+7
    return girls_age

buckys_limit = allowed_dating_age(22)
creppy_jow_limit = allowed_dating_age(49)
print("Bucky can date girls", buckys_limit,"or older")
print("Bucky can date girls", creppy_jow_limit,"or older")