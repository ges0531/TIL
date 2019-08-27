import sys


sys.stdin = open('input.txt', 'r')

x = int(input())

for i in range(x, 0, -1):
    print('{}{}{}'.format(' '*(3-i), '*'*(2*i-1), ' '*(3-i) ))
