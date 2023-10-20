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


'''mytext.txt:
01 a new beginning
02 developing
03 improving
04 finalizing
05 fin
'''

with open("Mytext.txt","r") as f:
    for line in f.read():
        print(line, end="")
