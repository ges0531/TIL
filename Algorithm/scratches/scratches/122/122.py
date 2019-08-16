import sys
sys.stdin = open("input.txt", "r")

T = list(map(int, input().split(' ')))

x = T[0]

if x % 400 == 0:
    print('leap year')
elif x % 4 == 0 and x % 100 != 0:
    print('leap year')
else:
    print('common year')