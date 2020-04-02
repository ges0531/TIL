import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    column, row, size = map(int, input().split())
    print(test_case)
    print(column, row, size)
    matrix = [0] * column
    dx = [-(size-2), size-2, -(size-2), size-2]
    dy = [-(size-2), -(size-2), size-2, size-2]
    my_max = 0
    for col in range(column):
        matrix[col] = list(map(int, input().split()))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            my_sum = 0
            location = [i+dx[0], j+dy[0]]
            for border in range(4):
                if i+dy[border] >= 0 and i+dy[border] < column:
                    if j+dx[border] >= 0 and j+dx[border] < row:
                        if location[0] >= 0 and location[0] < column:
                            if location[1] >= 0 and location[1] < row:
                                for _ in range(size-1):
                                    print(location[0], location[1], 'a')
                                    my_sum += matrix[location[0]+1][location[1]]
                                    location = [location[0]+1, location[1]]
                                for _ in range(size - 1):
                                    print(location[0], location[1], 'b')
                                    my_sum += matrix[location[0]][location[1]+1]
                                    location = [location[0], location[1]+1]
                                for _ in range(size - 1):
                                    print(location[0], location[1], 'c')
                                    my_sum += matrix[location[0]-1][location[1]]
                                    location = [location[0]-1, location[1]]
                                for _ in range(size - 1):
                                    print(location[0], location[1], 'd')
                                    my_sum += matrix[location[0]][location[1]-1]
                                    location = [location[0]-1, location[1]-1]
    print(my_sum)

    #         if my_sum > my_max:
    #     #             my_max = my_sum
    #     # print(my_max)