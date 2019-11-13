import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n, arr, result):
    global my_min, my_max, result_list
    if k == n:
        if my_min > result:
            my_min = result
        if my_max < result:
            my_max = result
    else:
        for a in range(k, n):
            arr[a], arr[k] = arr[k], arr[a]
            result_2 = result
            if arr[k] == '+':
                result = result + number_list[k+1]
            elif arr[k] == '-':
                result = result - number_list[k+1]
            elif arr[k] == '*':
                result = result * number_list[k+1]
            elif arr[k] == '/':
                result = int(result / number_list[k+1])
            perm(k+1, n, arr, result)
            result = result_2
            arr[a], arr[k] = arr[k], arr[a]


T = int(input())
T = 1

for test_case in range(1, T+1):
    number_count = int(input())
    operator_count = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    operator = ['+', '-', '*', '/']
    operator_list = []
    result_list = []
    my_min = 100000001
    my_max = -100000001
    for i in range(4):
        for j in range(operator_count[i]):
            operator_list.append(operator[i])
    perm(0, len(operator_list), operator_list, number_list[0])
    print('#{} {}'.format(test_case, my_max-my_min))
