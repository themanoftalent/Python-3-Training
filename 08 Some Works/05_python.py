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

players = [29, 58, 66, 71, 87]
print(dir(players))
print(type(players))

print("---------------------------")
pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

print("--------------------------------------------")


pow2 = []
for x in range(10):
   pow2.append(2 ** x)
   print(pow2)
