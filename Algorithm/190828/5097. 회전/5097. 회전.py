import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    number_count , work = map(int, input().split())
    nums = list(input().split())
    first = work % number_count
    print('#{} {}'.format(test_case, nums[first]))


