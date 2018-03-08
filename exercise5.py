a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newList = [] #new empty list

for i in a:
    if i in b and i not in newList:
        newList.append(i)

aList = "[{0}]".format(", ".join(str(i) for i in a))
bList = "[{0}]".format(", ".join(str(i) for i in b))
newListPrint = "[{0}]".format(", ".join(str(i) for i in newList))

print("List a: " + aList)
print("List b: " + bList)
print("Elements in both a & b: " + newListPrint)

test = list(set(a).intersection(set(b)))
if test:
    print("The intersections are: ", test)
else:
    print("No intersection.")