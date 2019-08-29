import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    paint = [list(map(int, input().split())) for _ in range(K)]
    matrix = [[0] * M for _ in range(N)]
    colors = [0] * (K+1)
    for i in range(K):
        colors[i] = paint[i][4]
    colors = set(colors)
    for column in range(len(paint)):
        a = 0
        for column_range in range(paint[column][0], paint[column][2] + 1):
            for row_range in range(paint[column][1], paint[column][3] + 1):
                if matrix[column_range][row_range] > paint[column][4]:
                    a = 1
                    break
        if a == 0:
            for column_range in range(paint[column][0], paint[column][2]+1):
                for row_range in range(paint[column][1], paint[column][3]+1):
                    matrix[column_range][row_range] = paint[column][4]
    my_box = []
    for color in colors:
        my_sum = 0
        for count_column in range(len(matrix)):
            my_sum += matrix[count_column].count(color)
        my_box.append(my_sum)
    print('#{} {}'.format(test_case, max(my_box)))


