#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    pattern = 'hackerrank'
    #dict = OrderedDict.fromkeys(s) 
    ptr=0
    for key in range(len(s)):
        if(s[key]==pattern[ptr]):
            ptr=ptr+1
        
        
        if(ptr==(len(pattern))):
            return 'YES'

        
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
