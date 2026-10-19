# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem
import math
import os
import random
import re
import sys
def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = str(first)
        next_num = first + 1

        while len(current) < len(s):
            current += str(next_num)
            next_num += 1

        if current == s:
            print("YES", first)
            return

    print("NO")
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
