import sys


sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
    print(test_case, '-')
    size = int(input())
    size = size + 2
    matrix = [[0]*size for _ in range(size)]
    for i in range(1, size-1):
        s = list(map(int, input().split()))
        matrix[i][1:size-1] = s[:]
    result = []

    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            location = [column, row]
            start_node = location
            x_count = y_count = 0
            if matrix[column][row]:
                while matrix[location[0]][location[1]+1]:
                    print(location, 1)
                    matrix[location[0]][location[1]] = 0
                    location[1] += 1
                    x_count += 1
                while matrix[location[0]+1][location[1]]:
                    print(location, 2)
                    matrix[location[0]][location[1]] = 0
                    location[0] += 1
                    y_count += 1
                result.append([y_count+1, x_count+1])
    print(result)
