n = int(input())
students = {}

for i in range(n):
    data = input().split()
    students[data[0]] = list(map(float, data[1:]))

name = input()
marks = students[name]

print("%.2f" % (sum(marks) / len(marks)))
