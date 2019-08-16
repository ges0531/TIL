import sys


sys.stdin = open('input.txt', 'r')

x = int(input())

for i in range(x):
    print(i+1, end=' ')