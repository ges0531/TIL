def power_set_r(k):
    global result
    if k == N:
        b = []
        for i in range(N):
            if arr[i]*a[i]:
                b.append(arr[i]*a[i])
        if sum(b) == 10:
            print(b)
    else:
        a[k] = 1
        power_set_r(k + 1)
        a[k] = 0
        power_set_r(k + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0] * len(arr)
N = len(arr)
power_set_r(0)