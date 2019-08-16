import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

x = T[0]

while x <= 15:
    print(x, end=' ')
    x = x + 1