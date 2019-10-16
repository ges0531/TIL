import sys

sys.stdin = open('input.txt', 'r')


def perm(k, N, arr):
    global result_list
    if k == N:
        arr_copy = arr[:]
        result_list.append(arr_copy)
    else:
        for ii in range(k, N):
            arr[ii], arr[k] = arr[k], arr[ii]
            perm(k+1, N, arr)
            arr[ii], arr[k] = arr[k], arr[ii]


matrix = [list(map(int, input().split())) for _ in range(10)]
matrix_copy = [[0]*10 for _ in range(10)]
for copy_1 in range(10):
    for copy_2 in range(10):
        matrix_copy[copy_1][copy_2] = matrix[copy_1][copy_2]
num_list = [i+1 for i in range(5)]
my_min = 10000000000000
result_list = []
b = 0
perm(0, len(num_list), num_list)

if matrix == [[0]*10 for _ in range(10)]:
    print(0)
else:
    for jj in range(len(result_list)):
        result = 0
        a = 1
        for j in range(4, -1, -1):
            my_rect = [[1] * result_list[jj][j] for _ in range(result_list[jj][j])]
            count = 0
            for column in range(len(matrix)-result_list[jj][j]+1):
                for row in range(len(matrix[column])-result_list[jj][j]+1):
                    my_list = []
                    for col_1 in range(result_list[jj][j]):
                        my_list_2 = []
                        for row_1 in range(result_list[jj][j]):
                            my_list_2.append(matrix[column+col_1][row+row_1])
                        my_list.append(my_list_2)
                    if my_list == my_rect:
                        count += 1
                        for col_2 in range(result_list[jj][j]):
                            for row_2 in range(result_list[jj][j]):
                                matrix[column + col_2][row + row_2] = 0
            if count > 5:
                a = 0
                break
            else:
                result += count
        if a:
            if my_min > result:
                my_min = result
        for copy_3 in range(10):
            for copy_4 in range(10):
                matrix[copy_3][copy_4] = matrix_copy[copy_3][copy_4]
    if my_min == 10000000000000:
        print(-1)
    else:
        print(my_min)
