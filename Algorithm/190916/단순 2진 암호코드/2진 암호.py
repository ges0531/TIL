import sys

sys.stdin = open('input.txt', 'r')


def start_node():
    start = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                start = [i, j]
                return start


T = int(input())

for test_case in range(1, T+1):
    password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    matrix_column, matrix_row = list(map(int, input().split()))
    matrix = [list(map(int, input())) for _ in range(matrix_column)]
    start_list = start_node()
    a = start_list[0]
    b = start_list[1]
    real_result = [0]*8
    real_result_2 = []
    odd_sum = 0
    even_sum = 0
    while matrix[a][b+55] == 0:
        b -= 1
    for i in range(8):
        result = [0]*7
        for j in range(7):
            result[j] = matrix[a][b]
            b += 1
        real_result[i] = result
    for k in range(len(real_result)):
        for l in range(len(password)):
            if real_result[k] == list(map(int, password[l])):
                real_result_2.append(l)
    for h in range(len(real_result_2)-1):
        if (h+1) % 2:
            odd_sum += real_result_2[h]
        else:
            even_sum += real_result_2[h]
    if ((3*odd_sum) + even_sum + real_result_2[-1]) % 10:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, odd_sum + even_sum + real_result_2[-1]))

