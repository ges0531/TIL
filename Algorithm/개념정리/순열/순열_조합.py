def perm(k, n, r):
    if k == r:
        print(a[:r])
    else:
        for i in range(k, n):
            a[k], a[i] = a[i], a[k]
            perm(k + 1, n, r)
            a[k], a[i] = a[i], a[k]


def comb(n, r):
    if r == 0:
        print(t)
    elif n < r:
        return
    else:
        t[r-1] = a[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


def power_set(k, n, tr):
    if k == n:
        print(tr)
    else:
        tr[k] = 1
        power_set(k+1, n, tr)
        tr[k] = 0
        power_set(k+1, n, tr)


a = [1, 2, 3, 4]
m = 2
t = [0]*m
perm(0, 4, m)
print()
comb(4, m)
print()
power_set(0, 3, [0]*3)