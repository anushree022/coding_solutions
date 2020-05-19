#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    arr1=[]
    for ind in range(len(arr)):
        v=arr.count(ind)      
        arr1.append(v)
        
    print(' '.join(map(str, arr1))) 


n = int(input())

arr = list(map(int, input().rstrip().split()))

countingSort(arr)

    