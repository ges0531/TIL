import sys

sys.stdin = open('input.txt', 'r')

size, length = map(int, input().split())
road_matrix = [list(map(int, input().split())) for _ in range(size)]
count = 0
# for row in range(size):
#     column_flag = 0
#     a = road_matrix[row][column_flag]
#     flag = 1
#     visited = [0]*size
#     while column_flag < size-1:
#         if flag == 0:
#             break
#         if a == road_matrix[row][column_flag+1]:
#             column_flag += 1
#         elif a - 1 == road_matrix[row][column_flag+1]:
#             flag = 1
#             for i in range(1, length+1):
#                 if road_matrix[row][column_flag+i] != a-1 or column_flag+length >= size:
#                     flag = 0
#                     break
#             if flag:
#                 for ii in range(1, length + 1):
#                     visited[column_flag + ii] = 1
#                 a = a-1
#                 column_flag += (length-1)
#         elif a + 1 == road_matrix[row][column_flag + 1]:
#             flag = 1
#             for i in range(length):
#                 if road_matrix[row][column_flag - i] != a or visited[column_flag - i]:
#                     flag = 0
#                     break
#             if flag:
#                 for ii in range(1, length):
#                     visited[column_flag - ii] = a+1
#                 a = a + 1
#                 column_flag += 1
#         else:
#             flag = 0
#     if flag:
#         count += 1
for column in range(size):
    row_flag = 0
    a = road_matrix[row_flag][column]
    flag = 1
    visited = [0] * size
    while row_flag < size-1:
        if flag == 0:
            break
        if a == road_matrix[row_flag+1][column]:
            row_flag += 1
        elif a - 1 == road_matrix[row_flag+1][column]:
            flag = 1
            for j in range(1, length+1):
                if road_matrix[row_flag+j][column] != a-1 or row_flag+length >= size:
                    flag = 0
                    break
            if flag:
                for jj in range(1, length + 1):
                    visited[row_flag + jj] = 1
                a = a-1
                row_flag += (length-1)
        elif a + 1 == road_matrix[row_flag + 1][column]:
            flag = 1
            for j in range(length):
                if visited[row_flag-j] != a or visited[row_flag - j]:
                    flag = 0
                    break
            if flag:
                a = a + 1
                row_flag += 1
        else:
            flag = 0
    if flag == 1:
        count += 1
        print(column, count)
print(count)
