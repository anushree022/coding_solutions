#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    no_array=[]
    string_lower=s.lower()
    for i in range(len(string_lower)):
        no_array.append(ord(string_lower[i]))
    for i in range(97,123):
        if i not in no_array:
            return 'not pangram'
        
    return 'pangram'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
