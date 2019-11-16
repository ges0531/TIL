import sys

sys.stdin = open('input.txt', 'r')

def comb(n, r, arr, t, k, s):
    if k == r:
        print(t)
    else:
        for i in range(s, n-r+k+1):
            t[k] = arr[i]
            comb(n, r, arr, t, k+1, i+1)


N, M = map(int, input().split())
comb(N, M, [i+1 for i in range(N)], [0]*M, 0, 0)
