import sys
import math
import random
import threading
import time
from functools import reduce

def binarysearch(arr, l ,u, x):
    while u >= 1:
        mid = l + (u - 1)/2;

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarysearch(arr, mid+1, u, x )
        else:
            return binarysearch(arr, l , mid-1, x)
    else:
        return -1

arr = [23,25,28,30,36,38,40]
x= 36
result = binarysearch(arr, 0, len(arr)-1, x)
if result != -1:
    print ("element is present at %d" % result)