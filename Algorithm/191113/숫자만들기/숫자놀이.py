import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n, arr, result):
    global my_min, my_max
    if k == n:
        if my_min > result:
            my_min = result
        if my_max < result:
            my_max = result
    else:
        for a in range(k, n):
            arr[a], arr[k] = arr[k], arr[a]
            result_2 = result
            if arr[0]:
                result = result + number_list[k + 1]
                arr[0] -= 1
                perm(k + 1, n, arr, result)
                arr[0] += 1
                result = result_2
            if arr[1]:
                result = result - number_list[k + 1]
                arr[1] -= 1
                perm(k + 1, n, arr, result)
                arr[1] += 1
                result = result_2
            if arr[2]:
                result = result * number_list[k + 1]
                arr[2] -= 1
                perm(k + 1, n, arr, result)
                arr[2] += 1
                result = result_2
            if arr[3]:
                result = int(result / number_list[k + 1])
                arr[3] -= 1
                perm(k + 1, n, arr, result)
                arr[3] += 1
                result = result_2
            arr[a], arr[k] = arr[k], arr[a]


T = int(input())
T = 1

for test_case in range(1, T+1):
    number_count = int(input())
    operator_count = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    my_min = 100000001
    my_max = -100000001
    perm(0, len(operator_count), operator_count, number_list[0])
    print(my_max, my_min)
    print('#{} {}'.format(test_case, my_max-my_min))