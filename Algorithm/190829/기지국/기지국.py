import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    size = size + 2
    matrix = [[0]*size for _ in range(size)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(1, size-1):
        s = list(input())
        matrix[i][1:size-1] = s[:]
    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 'A':
                for k in range(4):
                    if matrix[column+dy[k]][row+dx[k]] == 'H':
                        matrix[column + dy[k]][row + dx[k]] = 0
            elif matrix[column][row] == 'B':
                for k in range(4):
                    for B_count in range(1, 3):
                        if matrix[column+dy[k]*B_count][row+dx[k]*B_count] == 'H':
                            matrix[column + dy[k]*B_count][row + dx[k]*B_count] = 0
            elif matrix[column][row] == 'C':
                for k in range(4):
                    for C_count in range(1, 4):
                        if matrix[column+dy[k]*C_count][row+dx[k]*C_count] == 'H':
                            matrix[column + dy[k]*C_count][row + dx[k]*C_count] = 0
    count = 0
    one_list = sum(matrix, [])
    for cnt in one_list:
        if cnt == 'H':
            count += 1
    print(count)
