
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
