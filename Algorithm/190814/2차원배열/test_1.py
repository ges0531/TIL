matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        my_sum = 0
        for i in range(4):
            if column + dy[i] < 5 and column + dy[i] >= 0:
                if row + dx[i] < 5 and row + dx[i] >= 0:
                    my_sum += abs(matrix[column][row] - matrix[column + dy[i]][row + dx[i]])
        print('column: {} row: {} sum: {}'.format(column+1, row+1, my_sum))
