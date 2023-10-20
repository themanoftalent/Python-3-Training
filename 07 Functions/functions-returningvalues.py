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
    print(testfunc())
    print(testfuncNumber())
    print(testfuncRange())
    for n in testfuncRange():
        print(n, end = " ")

def testfunc():
    return 'This is a test function'

def testfuncNumber():
    return 42

def testfuncRange():
    return range(25)

if __name__ == "__main__": main()
