# Problem 15: Word Order
# https://www.hackerrank.com/challenges/word-order/problemn = int(input())
d = {}
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(len(d))
print(*d.values())
            
    
