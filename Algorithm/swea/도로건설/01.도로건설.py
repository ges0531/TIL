import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    copy_matrix = [[0] * size for _ in range(size)]
    my_min = 1000000000000
    result = []
    for i in range(5):
        for column in range(len(matrix)):
            for row in range(len(matrix[column])):
                count = 0
                count += abs((i+1)-matrix[column][row])
                for idx in range(1, (size-row)):
                    count += abs((i+1)-matrix[column][row+idx])
                    if count > my_min:
                        break
                for idx_2 in range(1, row+1):
                    count += abs((i+1)-matrix[column][row-idx_2])
                    if count > my_min:
                        break
                for idy in range(1, (size-column)):
                    count += abs((i+1)-matrix[column+idy][row])
                    if count > my_min:
                        break
                for idy_2 in range(1, column+1):
                    count += abs((i+1)-matrix[column-idy_2][row])
                    if count > my_min:
                        break
                if my_min >= count:
                    my_min = count
                    copy_matrix[column][row] = count
    for j in range(5):
        for column_2 in range(len(matrix)):
            for row_2 in range(len(matrix[column_2])):
                if copy_matrix[column_2][row_2] == my_min:
                    count = 0
                    count += abs((j + 1) - matrix[column_2][row_2])
                    for idx_3 in range(1, (size - row_2)):
                        count += abs((j + 1) - matrix[column_2][row_2 + idx_3])
                        if count > my_min:
                            break
                    for idx_4 in range(1, row_2 + 1):
                        count += abs((j + 1) - matrix[column_2][row_2 - idx_4])
                        if count > my_min:
                            break
                    for idy_3 in range(1, (size - column_2)):
                        count += abs((j + 1) - matrix[column_2 + idy_3][row_2])
                        if count > my_min:
                            break
                    for idy_4 in range(1, column_2 + 1):
                        count += abs((j + 1) - matrix[column_2 - idy_4][row_2])
                        if count > my_min:
                            break
                    if my_min >= count:
                        result.append(j+1)

    print('#{} {} {}'.format(test_case, my_min, min(result)))