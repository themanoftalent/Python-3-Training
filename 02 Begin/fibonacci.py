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

class fibon:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b


f = fibon(0, 1)
for r in f.series():
    if r > 200:
        break
    print(r)
