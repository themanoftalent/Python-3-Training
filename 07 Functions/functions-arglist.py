def main():
    testfunc(1,2,3)

# *args means optional arguments
def testfunc(arg1, *args):
    print(arg1, args)

if __name__ == "__main__": main()
