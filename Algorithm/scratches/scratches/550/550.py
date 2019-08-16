import sys


sys.stdin = open('input.txt', 'r')

x = int(input())

for i in range(x, 0, -1):
    for j in range(i):
        print('*', end='')
    print('')
for i in range(1, x+1):
    for j in range(i):
        print('*', end='')
    print('')
