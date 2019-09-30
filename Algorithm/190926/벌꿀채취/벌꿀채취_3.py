import sys

sys.stdin = open('input.txt', 'r')


def power_set(k, n, t, arr):
    global my_max, max_sum
    if k == n:
        real_sum = sum(t)
        if real_sum <= max_honey:
            my_sum = 0
            for i in range(select_honey):
                my_sum += t[i] ** 2
            if my_max < my_sum:
                my_max = my_sum
                max_sum = real_sum
    else:
        t[k] = arr[k]
        power_set(k+1, n, t, arr)
        t[k] = 0
        power_set(k+1, n, t, arr)


T = int(input())
T = 1
for test_case in range(1, T+1):
    size, select_honey, max_honey = map(int, input().split())
    honey_matrix = [list(map(int, input().split())) for _ in range(size)]
    sum_matrix = [[0]*size for _ in range(size)]
    result_matrix = [[0]*size for _ in range(size)]
    result = [0]*select_honey
    for column in range(len(honey_matrix)):
        for row in range(len(honey_matrix[column])):
            if row + select_honey <= size:
                my_max = 0
                for idx in range(select_honey):
                    result_matrix[column][row] += (honey_matrix[column][row+idx])**2
                    sum_matrix[column][row] += honey_matrix[column][row + idx]
                    result[idx] = honey_matrix[column][row+idx]
                if sum_matrix[column][row] > max_honey:
                    my_max = 0
                    max_sum = 0
                    power_set(0, select_honey, [0]*select_honey, result)
                    sum_matrix[column][row] = max_sum
                    result_matrix[column][row] = my_max
    for column_2 in range(len(honey_matrix)):
        for row_2 in range(len(honey_matrix[column_2])):
            if row_2 + select_honey <= size:
