import sys

sys.stdin = open('input.txt', 'r')


def perm(k, N, arr):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k+1, N, arr)
            arr[k], arr[i] = arr[i], arr[k]


def perm_2(k, N, arr, visited, t):
    if k == N:
        print(t)
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                t.append(arr[j])
                perm_2(k+1, N, arr, visited, t)
                t.pop()
                visited[j] = 0


def power_set(k, N, arr, t):
    if k == N:
        print(t)
    else:
        t[k] = arr[k]
        power_set(k+1, N, arr, t)
        t[k] = 0
        power_set(k + 1, N, arr, t)


def comb(n, r, arr, t):
    if r == 0:
        print(t)
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n-1, r, arr, t)


my_list = list(map(int, input().split()))
N = len(my_list)
my_list.sort()
# power_set(0, N, my_list, [0]*N)

for i in range(1, N+1):
    comb(N, i, my_list, [0]*i)