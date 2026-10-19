# Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

import math
import os
import random
import re
import sys

def marsExploration(s):
    changes = 0

    for i in range(len(s)):
        if s[i] != "SOS"[i % 3]:
            changes += 1
            
    return changes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
