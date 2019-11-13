import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n, arr):
    global my_min, my_max
    if k == n:
        print(arr)
    else:
        for a in range(k, n):
            arr[a], arr[k] = arr[k], arr[a]
            perm(k+1, n, arr)
            arr[a], arr[k] = arr[k], arr[a]


T = int(input())
T = 1

for test_case in range(1, T+1):
    number_count = int(input())
    operator_count = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    operator = ['+', '-', '*', '/']
    operator_list = []
    my_min = 100000000
    my_max = -100000000
    for i in range(4):
        for j in range(operator_count[i]):
            operator_list.append(operator[i])
    perm(0, len(operator_list), operator_list)
    # print('#{} {}'.format(test_case, my_max-my_min))