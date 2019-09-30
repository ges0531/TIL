def perm(k, n):
    if k == n:
        print(a)
    else:
        for i in range(k, n):
            a[k], a[i] = a[i], a[k]
            perm(k+1, n)
            a[k], a[i] = a[i], a[k]


def power_set(k, n):
    if k == n:
        print(t)
    else:
        t[k] = a[k]
        power_set(k+1, n)
        t[k] = 0
        power_set(k+1, n)


def comb(n, r):
    if r == 0:
        print(t)
    elif n < r:
        return
    else:
        t[r-1] = a[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


def DFS(start_node):
    stack = [start_node]
    visited = [0]*N
    while stack:
        a = stack.pop()
        if not visited[a]:
            visited[a] = 1






a = [2, 3, 1, 4]
t = [0, 0, 0, 0]
N = len(a)

# perm(0, N)
print()
power_set(0, N)
print()
# comb(N, 2)