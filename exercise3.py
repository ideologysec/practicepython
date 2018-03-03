# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# loops and conditionals and lists

fibList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

num = int(input("Please enter the largest num you would like in the list: "))

for i in fibList:
    if (i <= num):
        newList.append(i)

print("Done copying items to new list. New List is: ", newList)
