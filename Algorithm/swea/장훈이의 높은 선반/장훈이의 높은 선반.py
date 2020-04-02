import sys

sys.stdin = open('input.txt', 'r')


def power_set(k, n):
    global my_min
    if k == n:
        if sum(a) >= height:
            if my_min > sum(a):
                my_min = sum(a)
    else:
        a[k] = clerk_height[k]
        power_set(k+1, n)
        a[k] = 0
        power_set(k+1, n)


T = int(input())

for test_case in range(1, T+1):
    clerk, height = map(int, input().split())
    clerk_height = list(map(int, input().split()))
    n = len(clerk_height)
    a = [0]*n
    my_min = 100000000000000000000
    power_set(0, n)
    print('#{} {}'.format(test_case, my_min-height))