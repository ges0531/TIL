import sys

sys.stdin = open('input.txt', 'r')


def ladder_func():
    count = 0
    for i in range(matrix_column):
        y = 0
        x = i
        while y < matrix_row:
            if matrix[y][x] == 0:
                y += 1
            else:
                if x+1 < matrix_column:
                    if matrix[y][x+1]:
                        x += 1
                        y += 1
                    else:
                        x -= 1
                        y += 1
                else:
                    x -= 1
                    y += 1
        if x == i:
            count += 1
    if count == matrix_column:
        return True


def add_ladder():
    global result, my_min
    if result > 3:
        return -1
    else:
        for row in range(len(matrix)):
            for column in range(len(matrix[row])-1):
                if matrix[row][column] == 0:
                    matrix[row][column] = 1
                    matrix[row][column + 1] = 1
                    result += 1
                    if ladder_func():
                        if my_min > result:
                            my_min = result
                            return
                    add_ladder()
                    result -= 1
                    matrix[row][column] = 0
                    matrix[row][column + 1] = 0


matrix_column, ladder_count, matrix_row = map(int, input().split())
ladder_list = [list(map(int, input().split())) for _ in range(ladder_count)]
for minus in range(len(ladder_list)):
    ladder_list[minus][0] -= 1
    ladder_list[minus][1] -= 1
matrix = [[0]*matrix_column for _ in range(matrix_row)]
result = 0
my_min = 3
for ladder_line in range(len(ladder_list)):
    matrix[ladder_list[ladder_line][0]][ladder_list[ladder_line][1]] = 1
    matrix[ladder_list[ladder_line][0]][ladder_list[ladder_line][1]+1] = 1
add_ladder()
print(my_min)