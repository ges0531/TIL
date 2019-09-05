import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
T = 1
for test_case in range(1, T+1):
    print('#{}'.format(test_case))
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    result = []
    my_result = [0]*size
    for row in range(len(matrix[0])):
        for column in range(len(matrix)-1, -1, -1):
            result.append(matrix[column][row])
    for column_2 in range(len(matrix)-1, -1, -1):
        for row_2 in range(len(matrix[0])-1, -1, -1):
            result.append(matrix[column_2][row_2])
    for row_3 in range(len(matrix[0])-1, -1, -1):
        for column_3 in range(len(matrix)):
            result.append(matrix[column_3][row_3])

