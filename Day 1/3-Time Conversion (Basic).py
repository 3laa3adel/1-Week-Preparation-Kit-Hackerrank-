#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s2=""
    if s[-2]=='P':
        if s[0:2]!="12":
            if s[0]!='0':
                s2+=str(int(s[0:2])+12)
            elif s[0]=='0':s2+=str(int (s[1])+12)
        else:s2+=s[0:2]
        s2+=s[2:8]
    if s[-2]=='A':
        if s[0:2]=="12":
            s2+='00'
        else:
            s2+=s[0:2]
        s2+=s[2:8]
    return s2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
