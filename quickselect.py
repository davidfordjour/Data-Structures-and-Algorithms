import random
import timeit
from timeit import Timer
import matplotlib as plt

randomlist = random.sample(range(500), 10)                          # Creating a random list from 1-500 of 50 numbers

print(randomlist)

def partition(list,left,right):
    pivot_value = list[right]
    storeIndex = left

    for i in range(left, right):
        if list[i] <= pivot_value:
            list[storeIndex], list[i] = list[i], list[storeIndex]
            storeIndex += 1
   
    list[storeIndex], list[right] = list[right], list[storeIndex]
    return storeIndex


def select(list,left,right,k):
    if left == right:
        return list[left]

    pivotIndex = random.randrange(len(list)-1)

    pivotIndex = partition(list, left, right)

    if k == pivotIndex:
        return list[k]

    elif k < pivotIndex:
        return select(list, left, pivotIndex - 1, k)
    else:
        return select(list, pivotIndex + 1, right, k)


k = int(input("The kth smallest number you want: "))      # Asking the user to input the kth smallest number they want

print(select(randomlist,0, len(randomlist)-1,k))
print(partition(randomlist,0,len(randomlist)-1))

