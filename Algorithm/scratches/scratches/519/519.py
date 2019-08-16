import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

if T[0] == T[1]:
    print(1)
    print(0)
else:
    print(0)
    print(1)
