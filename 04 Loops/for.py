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

def main():

    # For loop can use any iterator.
    # be it file input, containers, strings
    fb = open('lines.txt')
    for line in fb.readlines():
        print(line, end = "")

    for each_number in (1,2,3,4,5):
        print(each_number)

    for each_number in [1,2,3,4,5]:
        print(each_number)

    for each_character in 'string':
        print(each_character)


    # How about index?
    for i, a_char in enumerate('this is a string'):
        if a_char == 's':
            print("Index {} is an s ".format(i))


if __name__ == "__main__": main()
