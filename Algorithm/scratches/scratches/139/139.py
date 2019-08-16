import sys


sys.stdin = open('input.txt', 'r')

x = list(map(int, input().split()))

y = x[0]
z = x[1]

if y >= 2 and y <= 9:
    if z >= 2 and z <= 9:
        if y > z:
            for j in range(1, 10):
                for i in range(y, z-1, -1):
                    print('{} * {} = {}'.format(i, j, i*j), end='   ')
                print('')
