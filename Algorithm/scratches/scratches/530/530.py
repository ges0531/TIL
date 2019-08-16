import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

if T[0] >= 20:
    print('adult')
else:
    print('{} years later'.format(20-T[0]))