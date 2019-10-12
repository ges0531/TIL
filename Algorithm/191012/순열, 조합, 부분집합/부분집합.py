import sys

sys.stdin = open('input.txt', 'r')


def power_set(k, N, arr, t):
    if k == N:
        print(t)
    else:
        t[k] = arr[k]
        power_set(k+1, N, arr, t)
        t[k] = 0
        power_set(k + 1, N, arr, t)
num_list = list(map(int, input().split()))
N = len(num_list)
t = [0]*N
power_set(0, N, num_list, t)