import sys

sys.stdin = open('input.txt', 'r')

matrix_row, matrix_column, shark_count = map(int, input().split())
shark_list = [list(map(int, input().split())) for _ in range(shark_count)]
result = 0
b = 0
print(shark_list)
for time in range(matrix_column):
    a = 1
    b += 1
    while a <= matrix_row:
        for i in range(len(shark_list)):
            if a == shark_list[i][0] and b == shark_list[i][1]:
                result += shark_list[i][4]
                shark_list.pop(i)
                break
        a += 1
    for j in range(len(shark_list)):
        count = 0
        while count - shark_list[j][2]:
            if shark_list[j][3] == 1:
                if shark_list[j][0] - 1 < 0:
                    shark_list[j][3] = 2
                    shark_list[j][0] += 1
                else:
                    shark_list[j][0] -= 1
            elif shark_list[j][3] == 2:
                if shark_list[j][0] + 1 > matrix_row:
                    shark_list[j][3] = 1
                    shark_list[j][0] -= 1
                else:
                    shark_list[j][0] += 1
            elif shark_list[j][3] == 3:
                if shark_list[j][1] + 1 > matrix_column:
                    shark_list[j][3] = 4
                    shark_list[j][1] -= 1
                else:
                    shark_list[j][0] += 1
            elif shark_list[j][3] == 4:
                if shark_list[j][1] - 1 < 0:
                    shark_list[j][3] = 3
                    shark_list[j][1] += 1
                else:
                    shark_list[j][0] -= 1
            count += 1
    print(shark_list)




