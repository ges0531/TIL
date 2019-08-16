import sys


sys.stdin = open('input.txt', 'r')

x = list(map(int,input().split()))
column = x[0]
row = x[1]

for i in range(1, column+1):
    for j in range(1, row+1):
        print(i * j, end=' ')
    print('')
