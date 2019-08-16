# import sys
#
#
# sys.stdin = open('input.txt', 'r')

count_odd = 0
count_even = 0
while True:
    x = int(input())
    if x == 0:
        break
    elif x % 2:
        count_odd += 1
    else:
        count_even += 1
print('odd: {}'.format(count_odd))
print('even: {}'.format(count_even))