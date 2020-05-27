#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    l_idx=0
    r_idx=len(arr)-1
    l_sum=arr[l_idx]
    r_sum=arr[r_idx]
    while l_idx!=r_idx:
        if l_sum<r_sum:
            l_idx += 1
            l_sum += arr[l_idx]
        else:
            r_idx -= 1
            r_sum += arr[r_idx]
    
    if l_sum==r_sum:
        return 'YES'
    return'NO'

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
