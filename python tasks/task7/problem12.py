# Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys

from collections import Counter

def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    common = count1 & count2

    return len(s1) + len(s2) - 2 * sum(common.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
