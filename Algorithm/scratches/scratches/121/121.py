import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

x = T[0]

if x == 0:
    print('zero')
elif x > 0:
    print('plus')
else:
    print('minus')
