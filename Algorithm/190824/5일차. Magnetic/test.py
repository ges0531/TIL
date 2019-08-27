import sys

sys.stdin = open('input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    size = int(input())
    matrix = [0] * size
    for i in range(size):
        matrix_column = list(map(int, input().split()))
        matrix[i] = matrix_column
    result = 0
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 1:
                for j in range(1, size-column):
                    if matrix[column+j][row] == 1:
                        break
                    elif matrix[column+j][row] == 2:
                        matrix[column][row] = matrix[column + j][row] = 0
                        result += 1
                        break
    print('#{} {}'.format(test_case, result))