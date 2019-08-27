import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    column, row, size = map(int, input().split())
    matrix = [0] * column
    dx = [0, 0, -(size-2), size-2, -(size-2), size-2, -(size-2), size-2]
    dy = [-(size-2), size-2, 0, 0, -(size-2), -(size-2), size-2, size-2]
    my_max = 0
    for col in range(column):
        matrix[col] = list(map(int, input().split()))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            my_sum = 0
            for border in range(8):
                if i+dy[border] >= 0 and i+dy[border] < column:
                    if j+dx[border] >= 0 and j+dx[border] < row:
                        my_sum += matrix[i+dy[border]][j+dx[border]]
            if my_sum > my_max:
                my_max = my_sum
    print('#{} {}'.format(test_case, my_max))