import sys

sys.stdin = open('input.txt', 'r')


def power_set(k, n):
    if k == n:
        print(a)
    else:
        a[k] = clerk_height[k]
        power_set(k+1, n)
        a[k] = 0
        power_set(k+1, n)


T = int(input())
T = 1

for test_case in range(1, T+1):
    clerk, height = map(int, input().split())
    clerk_height = list(map(int, input().split()))
    n = len(clerk_height)
    a = [0]*n
    power_set(0, n)