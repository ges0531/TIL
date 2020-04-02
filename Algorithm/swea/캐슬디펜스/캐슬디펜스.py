import sys

sys.stdin = open('input.txt')


def power_set(k, n, arr, t):
    global result
    if k == n:
        count = 0
        for i in range(n):
            if t[i] == 1:
                count += 1
        if count == 3:
            result.append(t[:])
    else:
        t[k] = arr[k]
        power_set(k+1, n, arr, t)
        t[k] = 0
        power_set(k + 1, n, arr, t)


def archer_attack(matrix_list, archer_list):
    count = 0
    for k in range(len(matrix_list)):
        if archer_list[k]:
            if matrix_list[k] == archer_list[k]:
                count += 1
    return count


matrix_column, matrix_row, attack = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
copy_matrix = matrix[:]
N = matrix_row
archer = [1]*N
result = []
my_max = 0
power_set(0, N, archer, [0]*N)
for kk in range(len(result)):
    real_count = 0
    for _ in range(matrix_column):
        for jj in range(attack-1, -1, -1):
            count = 0
            for k in range(matrix_row):
                if result[kk][k]:
                    flag = 0
                    for kkk in range(matrix_row//2):
                        if flag == 0:
                            if matrix[matrix_column-1-jj][k] == result[kk][k]:
                                count += 1
                                matrix[matrix_column - 1 - jj][k] = 0
                                flag = 1
                            elif k-kkk >= 0 and matrix[matrix_column-1-jj][k-kkk] == result[kk][k]:
                                count += 1
                                matrix[matrix_column - 1 - jj][k-kkk] = 0
                                flag = 1
                            elif k + kkk < matrix_row and matrix[matrix_column - 1 - jj][k + kkk] == result[kk][k]:
                                count += 1
                                matrix[matrix_column - 1 - jj][k + kkk] = 0
                                flag = 1
            real_count += count
        for j in range(matrix_column-1, -1, -1):
            if j == 0:
                matrix[j] = [0]*matrix_row
            else:
                matrix[j] = matrix[j-1]
        for h in matrix:
            print(h)
        print()
    if real_count > my_max:
        my_max = real_count
    matrix = copy_matrix
print(my_max)
