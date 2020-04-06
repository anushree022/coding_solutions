 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(n ,s, k):
    base=0
    end=0
    new_word=""
    k=k%26
    for i in range(n):
        ch= s[i]

        if(ch>="a" and ch<="z"):
            base=97
            end=122

        if(ch>='A' and ch<='Z'):
            base=65
            end=90

        if(base==97 or base==65):
            new_ord=ord(ch)+k

            if(new_ord>end):
                new_ord=base+(new_ord-end)-1
            ch=chr(new_ord)
        new_word =new_word+ch
        base=0
        end=0
    return new_word
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(n ,s, k)

    fptr.write(result + '\n')

    fptr.close()
