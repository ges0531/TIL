import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

if T[0] * T[1] * T[2] == 0:
    print(0)
else:
    print(1)