#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack=[]
    mp={'{':'}','(':')','[':']'}
    for i in range(len(s)): 
        if s[i] in ['{','(','[']: 
            stack.append(s[i])
        else: 
            if stack: 
                if s[i]!=mp[stack.pop()]:return "NO"
            else: 
                return "NO"
    return "NO" if stack else "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
