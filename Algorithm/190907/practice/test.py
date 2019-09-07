def perm(k):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[i], arr[k] = arr[k], arr[i]
            perm(k+1)
            arr[i], arr[k] = arr[k], arr[i]


def power_set(k):
    if k == N:
        print(a)
    else:
        a[k] = 1
        power_set(k+1)
        a[k] = 0
        power_set(k+1)


arr = [1, 2, 3]
N = len(arr)
a = [0] * N
perm(0)
print(1)
power_set(0)
