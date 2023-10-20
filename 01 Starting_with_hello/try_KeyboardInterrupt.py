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



while True:
    try:
        x = input("Whats up? \n ")
        if x == "quit":
            break
        print(x)
    except KeyboardInterrupt:
        print("to quit type any keys")
        continue
