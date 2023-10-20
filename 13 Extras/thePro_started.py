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

import webbrowser
import time

print ("this program started on " +time.ctime())
for x in range (0, 2):
    time.sleep (5)
    webbrowser.open("https://www.youtube.com/watch?v=ZNra8eK0K6k")
