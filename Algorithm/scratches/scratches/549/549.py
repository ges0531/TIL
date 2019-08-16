import sys


sys.stdin = open('input.txt', 'r')

x = int(input())
my_sum = 0
count = 0
i = 0
while my_sum < x:
    i += 1
    if i % 2:
        my_sum += i
        count += 1
print(count, my_sum)
