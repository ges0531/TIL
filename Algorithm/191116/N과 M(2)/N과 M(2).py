import sys

sys.stdin = open('input.txt', 'r')


def comb(n, r, arr, t):
    if r == 0:
        result_2 = [x for x in arr if x not in t]
        print(t, result_2)
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n-1, r, arr, t)

def comb_2(n, r, arr, t, k, s):
    if k == r:
        print(' '.join(map(str, t)))

    else:
        for i in range(s, n-r+k+1):
            t[k] = arr[i]
            comb_2(n, r, arr, t, k+1, i+1)

N, M = map(int, input().split())
comb(N, M, [i+1 for i in range(N)], [0]*M)
# comb_2(N, M, [i+1 for i in range(N)], [0]*M, 0, 0)