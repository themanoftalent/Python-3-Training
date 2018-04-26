#fibonnaci in a function
def funk(number):
    if number==1 or number==2:
        return 1
    return funk(number-1)+funk(number-2)

print(funk(8))
