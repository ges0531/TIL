import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n, r):
    if k == n:
        print(' '.join(map(str, a[0:r])))
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(k+1, n, r)
            a[i], a[k] = a[k], a[i]


N, M = map(int, input().split())
a = [0]*N
for j in range(N):
    a[j] = j+1
perm(0, N, M)
