#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    i = 0
    seaLevel = 0
    c = 0
    while i < len(s):
        if(s[i]=='U'):
            seaLevel+=1
            if(seaLevel==0):
                c+=1
        else:
            seaLevel-=1
        i+=1
    return c




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
