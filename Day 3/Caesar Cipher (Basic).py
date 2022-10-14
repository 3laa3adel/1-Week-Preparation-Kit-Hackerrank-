#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    o="abcdefghijklmnopqrstuvwxyz"
    k=int(k)%26
    a=o[k:]+o[0:k]
    s2=""
    for c in s: 
        upp=c.isupper()
        c=c.lower()
        if c in o:
            if upp :s2+=a[o.index(c)].upper()
            else:s2+=a[o.index(c)]
        else:s2+=c
    return s2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
