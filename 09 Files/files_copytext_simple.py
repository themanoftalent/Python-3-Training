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
    infile = open('lines.txt', 'r')
    outfile = open('output.txt', 'w')
    for line in infile:
        print(line, file = outfile, end = '')

if __name__ == "__main__": main()
