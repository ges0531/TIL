import sys

sys.stdin = open('input.txt', 'r')

matrix_row, matrix_column, shark_count = map(int, input().split())
shark_list = [list(map(int, input().split())) for _ in range(shark_count)]
row_short = (matrix_row-1)*2
column_short = (matrix_column-1)*2
for minus in range(len(shark_list)):
    shark_list[minus][0] -= 1
    shark_list[minus][1] -= 1
    if shark_list[minus][2] == 1 or shark_list[minus][2] == 2:
        shark_list[minus][2] = shark_list[minus][2] % row_short
    elif shark_list[minus][2] == 3 or shark_list[minus][2] == 4:
        shark_list[minus][2] = shark_list[minus][2] % column_short
result = 0
column = -1
for time in range(matrix_column):
    visited = [0] * len(shark_list)
    remove_list = []
    row = 0
    column += 1
    for _ in range(matrix_row):
        flag = 0
        for i in range(len(shark_list)):
            if row == shark_list[i][0] and column == shark_list[i][1]:
                result += shark_list[i][4]
                flag = 1
                shark_list.pop(i)
                visited.pop(i)
                break
        row += 1
        if flag:
            break
    for j in range(len(shark_list)-1, -1, -1):
        if shark_list[j][3] == 1:
            if 0 <= shark_list[j][0]-shark_list[j][2]:
                shark_list[j][0] = shark_list[j][0] - shark_list[j][2]
            else:
                shark_list[j][3] = 2
                if shark_list[j][2] - shark_list[j][0] < matrix_row:
                    shark_list[j][0] = shark_list[j][2] - shark_list[j][0]
                else:
                    shark_list[j][0] = matrix_row - (shark_list[j][2] - shark_list[j][0])
        elif shark_list[j][3] == 2:
            if shark_list[j][0]+shark_list[j][2] < matrix_row:
                shark_list[j][0] = shark_list[j][0] + shark_list[j][2]
            else:
                shark_list[j][3] = 1
                shark_list[j][0] = (shark_list[j][2] + shark_list[j][0]) - matrix_row
        elif shark_list[j][3] == 3:
            if shark_list[j][1]+shark_list[j][2] < matrix_column:
                shark_list[j][1] = shark_list[j][1] + shark_list[j][2]
            else:
                shark_list[j][3] = 4
                shark_list[j][1] = (shark_list[j][2] + shark_list[j][1]) - matrix_column
        elif shark_list[j][3] == 4:
            if 0 <= shark_list[j][1]-shark_list[j][2]:
                shark_list[j][1] = shark_list[j][1] - shark_list[j][2]
            else:
                shark_list[j][3] = 3
                if shark_list[j][2] - shark_list[j][1] < matrix_column:
                    shark_list[j][1] = shark_list[j][2] - shark_list[j][1]
                else:
                    shark_list[j][1] = matrix_column - (shark_list[j][2] - shark_list[j][1])
        visited[j] = 1
        for shark in range(len(shark_list)-1, -1, -1):
            if visited[shark] and j != shark:
                if shark_list[j][0] == shark_list[shark][0] and shark_list[j][1] == shark_list[shark][1]:
                    if shark_list[j][4] > shark_list[shark][4]:
                        shark_list.pop(shark)
                    else:
                        shark_list.pop(j)

print(result)
