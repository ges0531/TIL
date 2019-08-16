import sys
sys.stdin = open("input.txt", "r")

T = list(map(float, input().split(' ')))

first = T[0]
second = T[1]

if first >= 4 and second >= 4:
    print('A')
elif first >= 3 and second >= 3:
    print('B')
else:
    print('C')
