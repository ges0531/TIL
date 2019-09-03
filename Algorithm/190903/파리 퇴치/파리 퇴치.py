import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size, flapper_size = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    result = []


    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            my_sum = 0
            for fla_col in range(flapper_size):
                for fla_row in range(flapper_size):
                    if column+fla_col < size and row+fla_row < size:
                        my_sum += matrix[column+fla_col][row+fla_row]
            result.append(my_sum)
    print('#{} {}'.format(test_case, max(result)))
