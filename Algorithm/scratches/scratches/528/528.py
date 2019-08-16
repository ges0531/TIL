import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

if T[1] + 100 - T[0] > 0:
    print(T[1] + 100 - T[0])
    print('Obesity')
else:
    print(T[1] + 100 - T[0])