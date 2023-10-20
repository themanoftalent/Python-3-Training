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


class Parent:
    
    def print_last_name(self):
        print('Roberts')
    

class Child(Parent):
    
    def print_first_name(self):
        print('Bucky')
    
    def print_last_name(self):
        print('Snitzleberg')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()