import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print('#{}'.format(test_case))
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    result = []
    my_result = [0]*size
    real_list = []
    for row in range(len(matrix[0])):
        for column in range(len(matrix)-1, -1, -1):
            result.append(matrix[column][row])
    for column_2 in range(len(matrix)-1, -1, -1):
        for row_2 in range(len(matrix[0])-1, -1, -1):
            result.append(matrix[column_2][row_2])
    for row_3 in range(len(matrix[0])-1, -1, -1):
        for column_3 in range(len(matrix)):
            result.append(matrix[column_3][row_3])
    for i in range(len(result)//size):
        my_list = []
        for _ in range(size):
            my_list.append(result.pop(0))
        real_list.append(my_list)
    for k in range(size):
        ans = []
        for j in range(k, len(real_list), size):
            ans += real_list[j] + [' ']
        ans.pop()
        print(''.join(map(str, ans)))
