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


matrix_column, matrix_row, attack = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
copy_matrix = matrix[:]
N = matrix_row
archer = [1]*N
result = []
count = 0
my_max = 0
power_set(0, N, archer, [0]*N)
result_copy = result[:]
for jj in range(len(result)):
    count = 0
    visited = [[0]*matrix_row for _ in range(matrix_column)]
    for j in range(matrix_column-1, -1, -1):
        for kk in range(attack):
            for ii in range(1, (matrix_row // 2) + 1):
                result[jj] = result_copy[jj][:]
                for k in range(matrix_row):
                    if matrix[j-kk][k] == result[jj][k] and result[jj][k] == 1:
                        result[jj][k] = 0
                        if not visited[j-kk][k]:
                            count += 1
                        visited[j-kk][k] = 1
                    elif k-ii >= 0 and matrix[j-kk][k-ii] == result[jj][k] and result[jj][k] == 1:
                        result[jj][k] = 0
                        if not visited[j-kk][k-ii]:
                            count += 1
                        visited[j-kk][k-ii] = 1
                    elif k+ii < matrix_row and matrix[j-kk][k+ii] == result[jj][k] and result[jj][k] == 1:
                        result[jj][k] = 0
                        if not visited[j-kk][k+ii]:
                            count += 1
                        visited[j-kk][k+ii] = 1
    print(visited)
    print(count)
    if count > my_max:
        my_max = count
print(my_max)