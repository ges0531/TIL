import sys

sys.stdin = open('input.txt', 'r')


def comb(n, r, arr, t):
    if r == 0:
        print(t)
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n-1, r, arr, t)

num_list = list(map(int, input().split()))
N = len(num_list)
for i in range(1, N+1):
    t = [0]*i
    comb(N, i, num_list, t)
