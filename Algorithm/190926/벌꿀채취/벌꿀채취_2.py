import sys

sys.stdin = open('input.txt', 'r')


def power_set(k, n, t, arr, y, x):
    global my_max, location
    if k == n:
        if sum(t) <= max_honey:
            my_sum = 0
            for i in range(select_honey):
                my_sum += t[i]**2
            if my_max < my_sum:
                my_max = my_sum
                location = [y, x]
    else:
        t[k] = arr[k]
        power_set(k+1, n, t, arr, y, x)
        t[k] = 0
        power_set(k+1, n, t, arr, y, x)


T = int(input())

for test_case in range(1, T+1):
    size, select_honey, max_honey = map(int, input().split())
    honey_matrix = [list(map(int, input().split())) for _ in range(size)]
    my_max = 0
    my_max_2 = 0
    my_list = [0]*select_honey
    visited = [[0] * size for _ in range(size)]
    result = [0]*select_honey
    location = [0, 0]
    for _ in range(2):
        my_max = 0
        for column in range(len(honey_matrix)):
            for row in range(len(honey_matrix[column])):
                if not visited[column][row]:
                    if row + select_honey <= size:
                        for idx in range(select_honey):
                            result[idx] = honey_matrix[column][row+idx]
                        power_set(0, select_honey, [0]*select_honey, result, column, row)
        for idx_2 in range(select_honey):
            visited[location[0]][location[1]+idx_2] = 1
        my_max_2 += my_max
    print('#{} {}'.format(test_case, my_max_2))

