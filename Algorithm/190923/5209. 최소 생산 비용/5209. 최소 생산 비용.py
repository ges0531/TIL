import sys

sys.stdin = open('input.txt', 'r')


def perm(arr, k, n, result=0):
    global my_min
    if k == n:
        if result < my_min:
            my_min = result

    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            if result+factory[k][arr[k]] < my_min:
                perm(arr, k+1, n, result+factory[k][arr[k]])
            arr[i], arr[k] = arr[k], arr[i]


T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    factory = [list(map(int, input().split())) for _ in range(size)]
    a = [ii for ii in range(len(factory))]
    my_min = 1000000000000
    perm(a, 0, len(factory))
    print('#{} {}'.format(test_case, my_min))
