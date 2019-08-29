import sys


sys.stdin = open('input.txt', 'r')


T = int(input())
for test_case in range(1, T+1):
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
            start_location = [location[0], location[1]]
            x_count = y_count = 1
            if matrix[column][row]:
                while matrix[location[0]][location[1]+1]:
                    location[1] += 1
                    x_count += 1
                while matrix[location[0]+1][location[1]]:
                    location[0] += 1
                    y_count += 1
                for cnt in range(y_count):
                    for cnt_2 in range(x_count):
                        matrix[start_location[0]+cnt][start_location[1]+cnt_2] = 0

                result.append([y_count, x_count])
    result_list = []
    while len(result):
        first_rec = [result[0][0], result[0][1]]
        for column_2 in range(len(result)):
            if result[column_2][0] * result[column_2][1] < first_rec[0] * first_rec[1]:
                first_rec = [result[column_2][0], result[column_2][1]]
            elif result[column_2][0] * result[column_2][1] == first_rec[0] * first_rec[1]:
                if result[column_2][0] > first_rec[0]:
                    first_rec = [first_rec[0], first_rec[1]]
                else:
                    first_rec = [result[column_2][0], result[column_2][1]]
        result_list.append(result.pop(result.index(first_rec)))
    real_result = [len(result_list)] + sum(result_list, [])
    a = ' '.join(map(str, real_result))
    print('#{} {}'.format(test_case, a))
