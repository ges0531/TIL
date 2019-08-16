import sys
sys.stdin = open("input.txt", "r")

T = list(map(float, input().split(' ')))
weight = T[0]
if weight > 88.45:
    print('Heavyweight')
elif weight > 72.57:
    print('Cruiserweight')
elif weight > 61.23:
    print('Middleweight')
elif weight > 50.80:
    print('Lightweight')
else:
    print('Flyweight ')