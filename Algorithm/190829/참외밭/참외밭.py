import sys

sys.stdin = open('input.txt', 'r')

makuwa_count = int(input())
direction = area = [0] * 6
matrix = [list(map(int, input().split())) for _ in range(6)]
# line_list = [list(map(int, input().split())) for _ in range(6)]
compare_1 = compare_2 = count_one = count_two = count_tr = count_fo = 0
for i in range(len(matrix)):
    if matrix[i][0] == 1:
        compare_1 = matrix[i][1]
        count_one += 1
    elif matrix[i][0] == 3:
        compare_2 = matrix[i][1]
        count_tr += 1
for j in range(len(matrix)):
    if matrix[j][0] == 2:
        if matrix[j][1] > compare_1:
            compare_1 = matrix[j][1]
        count_two += 1
    elif matrix[j][0] == 4:
        if matrix[j][1] > compare_2:
            compare_2 = matrix[j][1]
        count_fo += 1




