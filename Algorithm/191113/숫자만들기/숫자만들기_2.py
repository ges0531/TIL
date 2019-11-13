import sys

sys.stdin = open('input.txt', 'r')

def calculate(result_list):

    for l in range(len(result_list)):
        if result_list[l] == '+':
            result_list[l + 1] = result_list[l-1] + result_list[l+1]
        elif result_list[l] == '-':
            result_list[l + 1] = result_list[l - 1] - result_list[l + 1]
        elif result_list[l] == '*':
            result_list[l + 1] = result_list[l - 1] * result_list[l + 1]
        elif result_list[l] == '/':
            result_list[l + 1] = int(result_list[l - 1] / result_list[l + 1])
    return result_list[-1]

def perm(k, n, arr, result):
    global my_min, my_max
    if k == n:
        if my_min > result:
            my_min = result
        # if my_max < result:
        #     my_max = result
    else:
        for a in range(k, n):
            arr[a], arr[k] = arr[k], arr[a]
            result_list = []
            for ii in range(k):
                result_list.append(number_list[ii])
                result_list.append(arr[ii])
            result_list.append(number_list[-1])
            result = calculate(result_list)
            if result < my_min:
                perm(k+1, n, arr, result)
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
    perm(0, number_count-1, operator_list, 0)
    print('#{} {}'.format(test_case, my_max-my_min))
