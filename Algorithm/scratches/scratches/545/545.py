import sys


sys.stdin = open('input.txt', 'r')

x = list(map(int,input().split()))
count_3 = 0
count_5 = 0
if len(x) == 10:
    for i in x:
        if i % 3 == 0 and i % 5 == 0:
            count_3 += 1
            count_5 += 1
        elif i % 3 == 0:
            count_3 += 1
        elif i % 5 == 0:
            count_5 += 1
print('Multiples of 3 : {}'.format(count_3))
print('Multiples of 5 : {}'.format(count_5))