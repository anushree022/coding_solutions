#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    
    for i in range(len(arr)):
        for i2 in range(i+1, len(arr)):
            if arr[i] + arr[i2] == m:
                return [i, i2]
 
            
    
 
 
t = int(input())

for t_itr in range(t):
    m = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result=icecreamParlor(m, arr)
    print (result[0]+1, result[1]+1)

        