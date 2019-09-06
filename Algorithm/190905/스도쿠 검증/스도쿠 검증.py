import sys

sys.stdin = open('input.txt', 'r')


def check(start_node):
    my_list = []
    for i in range(3):
        for j in range(3):
            my_list.append(matrix[start_node[0]+i][start_node[1]+j])
    if len(set(my_list)) == 9:
        return 1
    else:
        return 0

T = int(input())

for test_case in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    a = 0
    b = 0
    c = 0
    for column in range(len(matrix)):
        if a == 0:
            for i in range(len(matrix[0])):
                if a == 0:
                    for j in range(i+1, len(matrix[0])):
                        if matrix[column][i] == matrix[column][j]:
                            a = 1
                            break
    for column in range(len(matrix)):
        if b == 0:
            for i in range(len(matrix[0])):
                if b == 0:
                    for j in range(i+1, len(matrix[0])):
                        if matrix[i][column] == matrix[j][column]:
                            b = 1
                            break


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if check([i, j]) == 0:
                c = 1
    if a == 0 and b == 0 and c == 0:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))
