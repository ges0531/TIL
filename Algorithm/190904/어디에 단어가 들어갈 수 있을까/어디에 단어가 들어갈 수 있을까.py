import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size, length = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    a = 0
    for column in range(len(matrix)):
        result = [0] * size
        i = 0
        for row in range(len(matrix[0])):
            if matrix[column][row] == 0:
                i += 1
            else:
                result[i] += 1
        print(result)
        a += result.count(length)
    for row in range(len(matrix[0])):
        result = [0] * size
        i = 0
        for column in range(len(matrix)):
            if matrix[column][row] == 0:
                i += 1
            else:
                result[i] += 1
        a += result.count(length)
    # print('#{} {}'.format(test_case, a))


