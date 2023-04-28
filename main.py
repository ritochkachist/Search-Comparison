# Rita Chistiakova
# 4/26/2023
# Search Comparison Project

import random

def sequentialSearch(myList, target):
  for i in myList:
    if i == target:
      return True
  return False

def binarySearch(myList, start, end, target):
  if start <= end:
    mid = int((start + end) / 2)
    if myList[mid] == target:
      return True
    elif myList[mid] < target:
      return binarySearch(myList, target, mid + 1, end)
    else:
      return binarySearch(myList, target, start, mid - 1)
  else:
    return False 

# __________main part of program starts here__________
myList = []
for i in range(1000000):
  value = random.randint(0,1000001)
  myList.append(value)


print("About to start Sequential Search")
print(sequentialSearch(myList, 100100))
myList.sort()
print("About to start Binary Search")
print(binarySearch(myList, 100100, 0, len(myList) - 1))
#print(f"The sorted list: {myList}")