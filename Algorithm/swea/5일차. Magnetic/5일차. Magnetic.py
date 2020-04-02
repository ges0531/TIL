import sys

sys.stdin = open('input.txt', 'r')

T = 1

for test_case in range(1, T+1):
    # size = int(input())
    size = 7
    matrix = [0] * size
    dy = [-1, 1]
    for i in range(size):
        matrix_column = list(map(int, input().split()))
        matrix[i] = matrix_column
    count = 0
    result = 0
    print(matrix)
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 1:
                if matrix[column+1][row] == 0:
                    matrix[column][row] = 0
                    matrix[column+1][row] = 1
            elif matrix[column][row] == 2:
                if matrix[column-1][row] == 0:
                    matrix[column][row] = 0
                    matrix[column-1][row] = 2
    print(matrix)
    for column in range(len(matrix)):
        for row in range(len(matrix[0])-1):
            if matrix[row][column] == 1:
                if matrix[row+1][column] == 2:
                    matrix[row][column] = 0
                    matrix[row+1][column] = 0
                    result += 1
    # print(result)