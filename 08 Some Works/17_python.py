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


def add_numbers(*args):
  total = 0
  for a in args:
    total += a
  print(total)

add_numbers(3)
add_numbers(3, 32)
add_numbers(3, 43, 5453, 354234, 463463)
