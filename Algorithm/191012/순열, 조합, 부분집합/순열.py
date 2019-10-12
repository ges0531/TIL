import sys

sys.stdin = open('input.txt', 'r')


def perm(k, N, arr):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[i], arr[k] = arr[k], arr[i]
            perm(k+1, N, arr)
            arr[i], arr[k] = arr[k], arr[i]


num_list = list(map(int, input().split()))
N = len(num_list)
perm(0, N, num_list)
