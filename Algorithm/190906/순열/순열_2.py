def perm_3(k):
    if k == N:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[i], arr[k] = arr[k], arr[i]
            perm_3(k+1)
            arr[i], arr[k] = arr[k], arr[i]

arr = [1, 2, 3, 4, 5, 6, 7]
N = len(arr)
perm_3(0)