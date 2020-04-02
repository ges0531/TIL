import sys

sys.stdin = open('input.txt', 'r')

matrix_size = int(input())

matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
find_matrix_1 = [[1]*matrix_size for _ in range(matrix_size)]
find_matrix_2 = [[0]*matrix_size for _ in range(matrix_size)]
count_1 = 0
count_2 = 0
N = len(find_matrix_1)
M = len(find_matrix_2)
cut_count = 1
a = 1
while a:
    if matrix == find_matrix_1:
        count_1 += 1
        a = 0
    else:
        N = N//2
        find_matrix_1 = find_matrix_1[:N][:N]
        find_count = 0
        cut_count *= 4
        dx = [0, 0, 1, 1]
        dy = [0, 1, 0, 1]
        for cut in range(cut_count):
            find_count = 0
            for i in range(N):
                for j in range(N):
                    if matrix[i+dx[i]*cut_count][j+dy[i]*cut_count] == find_matrix_1[i][j]:
                        find_count += 1
        if find_count == N*N:
            count_1 += 1