
def main():
    testfunc(one = 1, two = 2, three = 3)
    testfunc2(5, 6, 7, 4, 5, one = 1, two = 2, three = 3)

def testfunc(**kwargs):
    print('This is a test function', kwargs['one'], kwargs['two'])

def testfunc2(this, that, other, *args, **kwargs):
    print("This, that, other: ", this, that, other)
    print("List arguments: ", args)
    print("Keyword arguments: ", kwargs['one'], kwargs['two'])

    # Since keyword arguments may not be known:
    for k in kwargs:
        print(k, kwargs[k])

    # Keyword arguments often used for parameters and switches
        
if __name__ == "__main__": main()
