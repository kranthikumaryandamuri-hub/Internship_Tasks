# Problem 13: Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problemif __name__ == '__main__':
    m = int(input())
    set_m = set(map(int, input().split()))

    n = int(input())
    set_n = set(map(int, input().split()))

    result = sorted(set_m.symmetric_difference(set_n))

    for num in result:
        print(num)
