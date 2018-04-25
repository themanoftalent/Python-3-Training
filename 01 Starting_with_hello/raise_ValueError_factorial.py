def fact(number):
    number = int(number)
    if number < 0:
        raise ValueError("Negative Value")
    pickNum = 1
    i = 1
    while i <= number:
        pickNum = pickNum * i
        i = i + 1
    return pickNum


print("It is : ", fact(int(input("Enter a number to calculate factorial value : \n"))))

print(7 * 720)
