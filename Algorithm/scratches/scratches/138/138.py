import sys


sys.stdin = open('input.txt', 'r')

x = int(input())

for i in range(1, x+1):
    for j in range(1, x+1):
        print('({}, {})'.format(i, j), end=' ')
    print('')