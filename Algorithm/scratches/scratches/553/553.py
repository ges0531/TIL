import sys


sys.stdin = open('input.txt', 'r')

x = int(input())

alpha = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(x, 0, -1):
    print('{}{}{}'.format())
