import sys

sys.stdin = open('input.txt', 'r')

matrix = [list(map(int, input().split())) for _ in range(5)]
moderator = [list(map(int, input().split())) for _ in range(5)]
moderator = sum(moderator, [])


def bingo():
    count = 0
    for i in range(len(moderator)):
        result = 0
        num = moderator[i]
        count += 1
        for j in range(len(matrix)):
            for k in range(len(matrix[j])):
                if matrix[j][k] == num:
                    matrix[j][k] = 0
        if count >= 12:
            for jj in range(5):
                flag_1 = 0
                flag_2 = 0
                for kk in range(5):
                    if matrix[jj][kk] == 0:
                        flag_1 += 1
                    if matrix[kk][jj] == 0:
                        flag_2 += 1
                if flag_1 == 5:
                    result += 1
                if flag_2 == 5:
                    result += 1
            if not (matrix[0][0] or matrix[1][1] or matrix[2][2] or matrix[3][3] or matrix[4][4]):
                result += 1
            if not (matrix[0][4] or matrix[1][3] or matrix[2][2] or matrix[3][1] or matrix[4][0]):
                result += 1
            if result >= 3:
                print(count)
                return


bingo()
