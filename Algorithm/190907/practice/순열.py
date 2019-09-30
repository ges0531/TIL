def perm(k):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[i], arr[k] = arr[k], arr[i]
            perm(k+1)
            arr[i], arr[k] = arr[k], arr[i]

def power_set_r(k):
    global result
    if k == N:
        b = []
        for i in range(N):
            if arr[i]*a[i]:
                b.append(arr[i]*a[i])
        result.append(b)
    else:
        a[k] = 1
        power_set_r(k + 1)
        a[k] = 0
        power_set_r(k + 1)


arr = [1, 2, 3, 4, 5]
a = [0] * len(arr)
N = len(arr)
result = []
perm(0)
print(1)
power_set_r(0)
print(result)