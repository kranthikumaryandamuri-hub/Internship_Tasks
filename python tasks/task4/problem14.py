# Problem 14: Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problemn = int(input())
stamps = set()

for _ in range(n):
    country = input().strip()
    stamps.add(country)

print(len(stamps))
