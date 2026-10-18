# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem
n = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    operation, size = input().split()
    other = set(map(int, input().split()))

    if operation == "intersection_update":
        A.intersection_update(other)
    elif operation == "update":
        A.update(other)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other)
    elif operation == "difference_update":
        A.difference_update(other)

print(sum(A))
