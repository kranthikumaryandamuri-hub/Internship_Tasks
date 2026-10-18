# Validating phone numbers
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        phone = input().strip()

        if re.fullmatch(r'[789]\d{9}', phone):
            print('YES')
        else:
            print('NO')
