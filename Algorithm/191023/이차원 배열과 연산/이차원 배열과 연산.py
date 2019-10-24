import sys

sys.stdin = open('input.txt', 'r')

r, c, result = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]
count = 0
num_count = [0] * 102
while matrix[r-1][c-1]-result:
    max_length = 0
    if len(matrix) >= len(matrix[0]):
        for column in range(len(matrix)):
            num_list = []
            for row in range(len(matrix[column])):
                num_count[matrix[column][row]] += 1
            for i in range(len(num_count)):
                if num_count[i]:
                    num_list.append([i, num_count[i]])
                    num_count[i] = 0
            for j in range(len(num_list)):
                num_list[j][0], num_list[j][1] = num_list[j][1], num_list[j][0]
            num_list.sort()
            for k in range(len(num_list)):
                num_list[k][0], num_list[k][1] = num_list[k][1], num_list[k][0]
            num_list = sum(num_list, [])
            matrix[column] = num_list
            N = len(num_list)
            if max_length < N:
                max_length = N
        for l in range(len(matrix)):
            if len(matrix[l])-max_length:
                for _ in range(abs(len(matrix[l])-max_length)):
                    matrix[l].append(0)
    else:
        for row_1 in range(len(matrix[0])):
            num_list_2 = []
            for col_1 in range(len(matrix)):
                num_count[matrix[col_1][row_1]] += 1
            for ii in range(len(num_count)):
                if num_count[ii]:
                    num_list_2.append([ii, num_count[ii]])
                    num_count[ii] = 0
            for jj in range(len(num_list_2)):
                num_list_2[jj][0], num_list_2[jj][1] = num_list_2[jj][1], num_list_2[jj][0]
            num_list_2.sort()
            for kk in range(len(num_list_2)):
                num_list_2[kk][0], num_list_2[kk][1] = num_list_2[kk][1], num_list_2[kk][0]
            num_list_2 = sum(num_list_2, [])
            matrix[col_1] = num_list_2
    count += 1
    print(matrix)
print(count)

