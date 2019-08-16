import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

x = T[0]
y = T[1]

if x > y:
    print(x - y)
else:
    print(y - x)