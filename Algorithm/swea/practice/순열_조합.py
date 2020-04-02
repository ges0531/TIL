def perm(k, n, r):
    if k == r:
        print(a[:r])
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(k+1, n, r)
            a[i], a[k] = a[k], a[i]


def power_set(t, k, n):
    if k == n:
        print(t)
    else:
        t[k] = a[k]
        power_set(t, k+1, n)
        t[k] = 0
        power_set(t, k+1, n)


def comb(n, r):
    if r == 0:
        print(t)
    elif n < r:
        return
    else:
        t[r-1] = a[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


a = [2, 3, 1, 4]
t = [0, 0, 0, 0]
N = len(a)
# perm(0, N, 2)
# power_set(t, 0, N)
comb(4, 2)