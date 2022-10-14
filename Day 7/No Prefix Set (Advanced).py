#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    def helper(l,word): 
        for i,c in enumerate(word):
            if c in l: 
                if l[c][1] or i==len(word)-1:return True
            else: 
                l[c]={},i==len(word)-1 
            l,nt=l[c]
        return False
    l={}
    for i in words: 
        if helper(l,i):print("BAD SET");print(i);return
    print("GOOD SET")
    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
