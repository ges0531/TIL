import sys

sys.stdin = open('input.txt', 'r')


matrix_column, matrix_row = map(int, input().split())

chess_list = [list(input()) for _ in range(matrix_column)]
a = [0, 1, 2, 3, 4, 5]
copy_1 = ['W', 'B']*4
copy_2 = ['B', 'W']*4
chess_copy_1 = [[] for _ in range(8)]
chess_copy_2 = [[] for _ in range(8)]
for co in range(4):
    chess_copy_1[2*co] = copy_1
    chess_copy_1[2*co+1] = copy_2
    chess_copy_2[2 * co] = copy_2
    chess_copy_2[2 * co + 1] = copy_1
my_min_1 = 1000000000000
my_min_2 = 1000000000000


for column in range(len(chess_list)):
    for row in range(len(chess_list[column])):
        if column+7 < matrix_column and row+7 < matrix_row:
            count_1 = 0
            for i in range(8):
                for j in range(8):
                    if chess_list[column+i][row+j] != chess_copy_1[i][j]:
                        count_1 += 1
            if count_1 < my_min_1:
                my_min_1 = count_1
for column_2 in range(len(chess_list)):
    for row_2 in range(len(chess_list[column_2])):
        if column_2+7 < matrix_column and row_2+7 < matrix_row:
            count_2 = 0
            for ii in range(8):
                for jj in range(8):
                    if chess_list[column_2+ii][row_2+jj] != chess_copy_2[ii][jj]:
                        count_2 += 1
            if count_2 < my_min_2:
                my_min_2 = count_2
if my_min_1 > my_min_2:
    print(my_min_2)
else:
    print(my_min_1)