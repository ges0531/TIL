import sys

sys.stdin = open('input.txt', 'r')


def end_node():
    end = []
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])-1, -1, -1):
            if matrix[i][j] == 1:
                end = [i, j]
                return end

T = int(input())
T = 1

for test_case in range(1, T+1):
    password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    matrix_column, matrix_row = list(map(int, input().split()))
    matrix = [list(map(int, input())) for _ in range(matrix_column)]
    end_list = end_node()
    a = end_list[0]
    b = end_list[1]
    print(a, b)
    while matrix[a][b]:
        if matrix[a][b]:
            a -= 1
    a += 1
    print(a, b)