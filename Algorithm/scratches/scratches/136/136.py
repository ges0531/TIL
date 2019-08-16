import sys


sys.stdin = open('input.txt', 'r')

x = int(input())

for i in range(1, 11):
    print(i * x, end=' ')