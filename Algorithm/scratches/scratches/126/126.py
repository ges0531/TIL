import sys


sys.stdin = open('input.txt', 'r')

count_odd = 0
count_even = 0
while True:
    x = list(map(int, input().split()))
    for i in x:
        if i == 0:
            break
        elif i % 2:
            count_odd += 1
        else:
            count_even += 1
    break
print('odd : {}'.format(count_odd))
print('even : {}'.format(count_even))