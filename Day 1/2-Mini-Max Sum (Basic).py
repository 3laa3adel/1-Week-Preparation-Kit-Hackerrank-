#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr=sorted(arr)
    mn,mx=0,0
    for i in range(len(arr)-1):mn+=arr[i]
    for i in range(1,len(arr)):mx+=arr[i]
    print(str(mn)+' '+str(mx))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
