# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Exercise 6: String indexes

inputList = input("Please enter a string and I'll tell you if it's a palindrome: ").replace(" ", "").lower()

if(inputList[::1]==inputList[::-1]):
    print("You have found a palindrome!")
else:
    print("Sorry, this is not a palindrome")

"""
if (listLen % 2) is not 0:
    print("Unfortunately, we need an even number of letters for a word to be a palindrome")
    quit()


for i in inputList:
    print("i is currently: ", i, " and endIndex is currently: ", endIndex)
    if not (i == inputList[endIndex]):
        print("This is not a palindrome, unfortunately")
        quit()
    else:
        endIndex -= 1
        pass

print("Your word appears to be a palindrome!")
"""