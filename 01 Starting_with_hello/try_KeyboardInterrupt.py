while True:
    try:
        x = input("Whats up? \n ")
        if x == "quit":
            break
        print(x)
    except KeyboardInterrupt:
        print("to quit type any keys")
        continue
