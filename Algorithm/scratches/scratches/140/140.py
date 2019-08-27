import sys


sys.stdin = open('input.txt', 'r')

count = 0
my_sum = 0
while count < 19:
    x = list(map(int, input().split()))
    for i in x:
        if i == 0:
            break
        else:
            my_sum += i
            count += 1

print(my_sum, my_sum//count)