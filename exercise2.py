# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# modulo practice, mostly

incomingNumber = input("Enter your age: ")
incomingNumber = int(incomingNumber)

if (not incomingNumber % 2):
    print("You entered an even number")

else:
    print("You entered an odd number")
