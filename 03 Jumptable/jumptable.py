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


class jumpingTable():
    jumpingTable = {}

    def set(self, n, i):
        self.jumpingTable[n] = i

    def going(self, index):
        if index in self.jumpingTable:
            self.jumpingTable[index]()
        elif 'default' in self.jumpingTable:
            self.jumpingTable['default']()
        else:
            raise RuntimeError('undefined jumping: {}'.format(index))

def main():
    j = jumpingTable();
    j.set('one', one)
    j.set('two', two)
    j.set('three', three)
    j.set('default', default)

    try:
        j.going('seven')
    except RuntimeError as e:
        print(e)

def one():
    print('This is the "one" function.')

def two():
    print('This is the "two" function.')

def three():
    print('This is the "three" function.')

def default():
    print('this is the default function.')

if __name__ == "__main__": main()
