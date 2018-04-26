'''• 2! = 2.1 = 2
• 3! = 3.2.1 = 3.2! = 3.2 = 6
• 4! = 4.3.2.1 = 4.3! = 4.3.2! = 4.3.2 = 24
• 5! = 5.4.3.2.1 = 5.4! = 5.4.3! = 5.4.6 = 20.6 = 120
• 6! = 6.5.4.3.2.1 = 6.5! = 6.120 = 720
• 7! = 7.6.5.4.3.2.1 = 7.6! = 7.720 = 5040 '''


def factorialz(number):

    if number == 0:
        return 1
    return number * factorialz(number - 1)


print(factorialz(5))

#print("Another  method")
'''
import math
math.factorial(n)
'''
