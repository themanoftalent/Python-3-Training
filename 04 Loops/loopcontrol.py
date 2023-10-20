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
    satring = 'this is a string'

    # Print string and skip all s's.
    for c in satring:
        if c == 'satring':
            continue
        print(c, end='')

    print()
    # Print string and stop at first s.
    for c in satring:
        if c == 'satring':
            break
        print(c, end='')

    print()

    # For Loop Else continues after last iterator value.
    for c in satring:
        print(c, end='')
    else:
        print(" else ")


if __name__ == "__main__": main()
