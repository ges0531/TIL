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
    row = 0
    column += 1
    for _ in range(matrix_row):
        flag = 0
        for i in range(len(shark_list)):
            if row == shark_list[i][0] and column == shark_list[i][1]:
                result += shark_list[i][4]
                print(result)
                flag = 1
                shark_list.pop(i)
                break
        row += 1
        if flag:
            break
    for j in range(len(shark_list)):
        for _ in range(shark_list[j][2]):
            if shark_list[j][3] == 1:
                shark_list[j][0] -= 1
                if shark_list[j][0] < 0:
                    shark_list[j][3] = 2
                    shark_list[j][0] += 2
            elif shark_list[j][3] == 2:
                shark_list[j][0] += 1
                if shark_list[j][0] > matrix_row-1:
                    shark_list[j][3] = 1
                    shark_list[j][0] -= 2
            elif shark_list[j][3] == 3:
                shark_list[j][1] += 1
                if shark_list[j][1] > matrix_column-1:
                    shark_list[j][3] = 4
                    shark_list[j][1] -= 2
            elif shark_list[j][3] == 4:
                shark_list[j][1] -= 1
                if shark_list[j][1] < 0:
                    shark_list[j][3] = 3
                    shark_list[j][1] += 2
    print(shark_list)
    remove_list = []
    for shark_1 in range(len(shark_list)):
        for shark_2 in range(shark_1+1, len(shark_list)):
            if shark_list[shark_1][0] == shark_list[shark_2][0] and shark_list[shark_1][1] == shark_list[shark_2][1]:
                if shark_list[shark_1][4] > shark_list[shark_2][4]:
                    remove_list.append(shark_list[shark_2])
                else:
                    remove_list.append(shark_list[shark_1])
    for rem in range(len(remove_list)):
        if remove_list[rem] in shark_list:
            shark_list.remove(remove_list[rem])
print(result)




