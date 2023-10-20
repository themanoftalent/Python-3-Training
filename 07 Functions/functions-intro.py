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
    testfunc(42)
    testfunc(42, 50)

# Adding default values to method arguments makes those arguments optional.
# If you want the value to be optional but have no value, specify the value 'None'
def testfunc(arg1, arg2 = None, arg3 = 10):
#    pass
    # Check for no argument
    if arg2 is None:
        arg2 = 600
    print('This is a test function')
    print("Argument = ", arg1, arg2, arg3)


if __name__ == "__main__": main()
