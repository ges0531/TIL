import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    count = 0
    odd_index = []
    even_index = []
    matrix = [[0] * 10 for _ in range(10)]
    color_range = int(input())
    for N in range(color_range):
        color = list(map(int, input().split()))
        for i in range(color[0], color[2]+1):
            for j in range(color[1], color[3]+1):
                if matrix[i][j] != color[4]:
                    matrix[i][j] += color[4]
                if matrix[i][j] == 3:
                    count += 1
    # for my_count in range(10):
    #     count += matrix[my_count].count(3)

    print('#{} {}'.format(test_case, count))