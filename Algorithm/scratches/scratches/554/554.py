import sys


sys.stdin = open('input.txt', 'r')

x = int(input())
nums = [1, 2, 3, 4, 5, 6]
alpha = ['A', 'B', 'C', 'D', 'E', 'F']
k = 0
for i in range(x):
    for j in range(x+1):
        print(nums[k], end='')
        k += 1
    print('')