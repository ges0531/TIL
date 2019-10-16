import sys

sys.stdin = open('input.txt', 'r')


def rect(k, arr):
    global count
    my_rect = [[1]*k for _ in range(k)]
    for column in range(len(arr)):
        for row in range(len(arr[column])):
            my_list_1 = []
            for col_1 in range(len(my_rect)):
                my_list_2 = []
                for row_1 in range(len(my_rect[col_1])):
                    my_list_2.append(arr[column+col_1][row+row_1])
                my_list_2.append(my_list_1)
            if my_list_2 == my_rect:
                count += 1
                for col_2 in range(k):
                    for row_2 in range(k):
                        arr[column + col_2][row + row_2] = 0

matrix = [list(map(int, input().split())) for _ in range(10)]
