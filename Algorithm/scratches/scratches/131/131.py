import sys


sys.stdin = open('input.txt', 'r')

x = list(map(int,input().split()))

y = x[0]
z = x[1]

if y > z:
    for i in range(z, y+1):
        print(i, end=' ')
else:
    for i in range(y, z+1):
        print(i, end=' ')