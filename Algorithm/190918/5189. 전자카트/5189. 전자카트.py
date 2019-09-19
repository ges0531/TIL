def perm(k, N):
    global my_min, my_sum
    if k == N:
        arr_2 = arr + [0]
        for k in range(len(arr_2)-1):
            my_sum += magnetic_cart[arr_2[k]][arr_2[k+1]]
        if my_sum < my_min:
            my_min = my_sum
        my_sum = 0

    else:
        if arr[0] == 0:
            for i in range(k, N):
                arr[i], arr[k] = arr[k], arr[i]
                perm(k+1, N)
                arr[i], arr[k] = arr[k], arr[i]


T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    magnetic_cart = [list(map(int, input().split())) for _ in range(size)]
    arr = [0]*size
    my_min = 1000000000000
    my_sum = 0
    for j in range(size):
        arr[j] = j
    perm(0, size)
    print('#{} {}'.format(test_case, my_min))