
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    n = len(w)
    j=i=s=0
    t=1
    while(i < n):
        k = w[j]+4
        if(w[i] <= k):
            s += 1
            i += 1
        else:
            t += 1
            j = s
    return t
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
