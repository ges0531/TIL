import sys


sys.stdin = open('input.txt', 'r')

count = 0

while True:
    x = list(map(int, input().split()))
    for i in x:
        if i == 0:
            break
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        else:
            count += 1
    break
print(count)
