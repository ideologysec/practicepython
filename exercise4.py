# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# loops and conditionals and lists

num = int(input("Please enter the number you would like factored: "))

divList = range(1, num+1)
newList = []

for i in divList:
    if (not num % i):
        newList.append(i)

# shorter printout
# print("Here are the factors of your number: ", newList)

print("Here are the factors of your number:")
for element in newList:
    print (element)
