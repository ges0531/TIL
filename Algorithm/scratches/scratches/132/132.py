import sys


sys.stdin = open('input.txt', 'r')

x = int(input())
my_sum = 0
for i in range(x+1):
    if i % 5 == 0:
        my_sum += i
print(my_sum)