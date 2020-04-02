import sys


sys.stdin = open('input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    case_num = int(input())
    matrix = []
    for i in range(1, 101):
        string = list(input())
        matrix.append(string)
    length = len(matrix)
    a = 1
    while a != 0:
        index_num = -1
        column_box = row_box = [0] * length
        for k in range(len(matrix[0])-length+1):
            index_num += 1
            for column in range(len(matrix)):
                for j in range(length):
                    column_box[j] = matrix[column][j+index_num]
                if column_box == column_box[::-1]:
                    a = 0
            for row in range(len(matrix[0])):
                for l in range(length):
                    row_box[l] = matrix[l+index_num][row]
                if row_box == row_box[::-1]:
                    a = 0
        length -= 1
    print('#{} {}'.format(test_case, length+1))