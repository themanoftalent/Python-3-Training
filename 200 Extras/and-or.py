print("Enter a number between 5 and 15")
n = input()
if n < 5 or n > 15:
    print("I don't like that number.")
else:
    print("Thank you, that's a great number.")

print("Enter a number between 11 and 1100")
i = input()
if i > 11 or i < 1100:
    print("I like that number.")
elif i == 11 or i == 1100:
    print("You just have to test my limits, don't you?")
else:
    print("Now you're just pressing my buttons.")

print("Enter a number between 1 and 28")
s = input()
if s >= 1 or s <= 28:
    print("On February {}, let's go sledding.".format(s))
else:
    print("February doesn't have that day.")
