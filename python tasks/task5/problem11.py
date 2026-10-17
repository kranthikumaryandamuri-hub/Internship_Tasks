# Text Wrap
# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

s = input()
width = int(input())

print(textwrap.fill(s, width))
