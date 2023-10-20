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
# create and open a file

with open("NewFile.txt", "a+") as f:
    f.write("We are writing some new text here.")
    f.close()

f = open("NewFile.txt", "r+")
radme = f.read(33)
print(radme)
f.close()
