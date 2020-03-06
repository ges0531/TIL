import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n, arr, result_arr, result=0):
    global my_min
    if k == n:
        if result < my_min:
            my_min = result
    else:
        for j in range(k, n):
            arr[k], arr[j] = arr[j], arr[k]
            if (result+result_arr[k][arr[k]]) < my_min:
                perm(k+1, n, arr, result_arr, result+result_arr[k][arr[k]])
            arr[k], arr[j] = arr[j], arr[k]


T = int(input())
for test_case in range(1, T+1):
    test_case_num = int(input())
    cookie_matrix = [list(map(int, input().split())) for _ in range(10)]
    cookie_location = [[] for _ in range(6)]
    robot_track = [[] for _ in range(6)]
    index = 0
    my_min = 100000000000
    a = [z for z in range(6)]
    for column in range(len(cookie_matrix)):
        for row in range(len(cookie_matrix[column])):
            if cookie_matrix[column][row] == 1:
                cookie_location[0] = [column, row]
            elif cookie_matrix[column][row] == 2:
                cookie_location[1] = [column, row]
            elif cookie_matrix[column][row] == 3:
                cookie_location[2] = [column, row]
            elif cookie_matrix[column][row] == 4:
                cookie_location[3] = [column, row]
            elif cookie_matrix[column][row] == 5:
                cookie_location[4] = [column, row]
            elif cookie_matrix[column][row] == 6:
                cookie_location[5] = [column, row]
    for column_2 in range(len(cookie_matrix)):
        for row_2 in range(len(cookie_matrix[column_2])):
            if cookie_matrix[column_2][row_2] == 9:
                for i in range(6):
                    robot_track[index].append(abs(column_2-cookie_location[i][0])+abs(row_2-cookie_location[i][1]))
                index += 1
    perm(0, 6, a, robot_track)
    print('#{} {}'.format(test_case, my_min))
