#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    ls_important = []
    sum1 = 0

    for i in range(len(contests)):
        li, ti=contests[i]
        if ti==0:
            sum1 = sum1 + li
        else:
            ls_important.append(li)
    balance=[]
    ls_important.sort()
    if k>0:
        sum4 = sum(ls_important[0:-k] )
        del ls_important[0:-k]  
        sum2 = sum(ls_important)-sum4
        sum3 = (sum2+sum1)
    else:
        sum3 =0
        for i in range(len(ls_important)):
            sum3= sum3 + ls_important[i]
        sum3= sum3+sum1
    
    return sum3



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
