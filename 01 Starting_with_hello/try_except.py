while True:
    aNumber = input("Enter a number: ")
    if not aNumber:
        break
    try:
        aNumber=int(aNumber)
    except ValueError:
        print("Invalid input")
        continue
    print((aNumber) ** 2)
