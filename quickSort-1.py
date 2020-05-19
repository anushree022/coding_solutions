#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    
    left=[]
    right=[]
    equal = []
    pivot= arr[0]
    for i in range(len(arr)):
        if arr[i]< pivot:
            left.append(arr[i])
        elif arr[i]> pivot:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    combine = left+equal+right
    return combine

    m = input()
arr = [int(i) for i in input().strip().split()]
arr = quickSort(arr)
print (' '.join(map(str, arr)))