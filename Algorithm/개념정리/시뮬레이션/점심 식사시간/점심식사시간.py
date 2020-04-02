import sys

sys.stdin = open('input.txt')


def comb(n, r, arr, t):
    global my_min
    if r == 0:
        result_1 = t[:]
        result_2 = []
        for jj in range(len(arr)):
            if arr[jj] not in result_1:
                result_2.append(arr[jj])
        for li_1 in range(len(result_1)):
            result_1[li_1] = abs(result_1[li_1][0] - exit_1[0][0]) + abs(result_1[li_1][1] - exit_1[0][1])
        for li_2 in range(len(result_2)):
            result_2[li_2] = abs(result_2[li_2][0] - exit_2[0][0]) + abs(result_2[li_2][1] - exit_2[0][1])
        result_1.sort(reverse=True)
        result_2.sort(reverse=True)
        stair_1 = []
        stair_2 = []
        time = 0
        flag_count = 0
        while result_1 or result_2 or flag_count != len(arr):
            count_1 = 0
            count_2 = 0
            for move_1 in range(len(result_1)-1, -1, -1):
                result_1[move_1] -= 1
                if result_1[move_1] == 0:
                    result_1.pop(move_1)
                    stair_1.append(matrix[exit_1[0][0]][exit_1[0][1]])
            for move_2 in range(len(result_2)-1, -1, -1):
                result_2[move_2] -= 1
                if result_2[move_2] == 0:
                    result_2.pop(move_2)
                    stair_2.append(matrix[exit_2[0][0]][exit_2[0][1]])
            for stair in range(len(stair_1)):
                if stair_1[stair]:
                    stair_1[stair] -= 1
                    count_1 += 1
                    if stair_1[stair] == 0:
                        flag_count += 1
                if count_1 >= 3:
                    break
            for stair in range(len(stair_2)):
                if stair_2[stair]:
                    stair_2[stair] -= 1
                    count_2 += 1
                    if stair_2[stair] == 0:
                        flag_count += 1
                if count_2 >= 3:
                    break
            time += 1
        if my_min > time:
            my_min = time
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n - 1, r, arr, t)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    exit_1 = []
    exit_2 = []
    location = []
    my_min = 100000000
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 1:
                location.append([row, column])
            elif matrix[row][column] > 1:
                exit_1.append([row, column])
    exit_2.append(exit_1.pop())
    for i in range(len(location)+1):
        visited = [0]*len(location)
        comb(len(location), i, location, [0]*i)
    my_result = my_min+2
    print('#{} {}'.format(test_case, my_result))