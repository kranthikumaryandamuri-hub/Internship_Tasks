# Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    previous_char = ""

    for char in s:
        value = ord(char) - ord('a') + 1

        if char == previous_char:
            current_weight += value
        else:
            current_weight = value

        weights.add(current_weight)
        previous_char = char

    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
