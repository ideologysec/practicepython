# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# modulo practice, mostly

incomingNumber = input(
    "Please enter a number (and I'll tell you if it's even or odd: ")
incomingNumber = int(incomingNumber)

if (not incomingNumber % 2):
    if (not incomingNumber % 4):
        print("Your number was a multiple of four (and therefore even)!")
    else:
        print("You entered an even number.")

else:
    print("You entered an odd number.")


num = input("Now, let's get fancy. Please enter a dividend: ")
num = int(num)

check = input("Please enter your divisor: ")
check = int(check)

if (not num % check):
    print("Your dividend is evenly divisible by your divisor (the remainder is 0)")

else:
    print("No even diviision here! Your remainder is " + str(num % check))
