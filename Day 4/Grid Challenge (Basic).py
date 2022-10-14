#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i]=list(grid[i])
        grid[i].sort()
        grid[i]=''.join(grid[i])

    for i in range(len(grid[0])):
        l=[]
        for j in range(len(grid)):
            l.append(grid[j][i])
        if l!=sorted(l):return("NO")
    return ("YES")

    
    print(grid)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
