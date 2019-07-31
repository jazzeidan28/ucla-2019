import random


aList = []
for unused in range(10):
    aList.append(random.randint(0,57))
print(aList)

total = 0
for x in aList:
    total = total + x
print(total)