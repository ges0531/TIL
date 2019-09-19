import sys

sys.stdin = open('input.txt', 'r')


def backtracking(idx, idy, result):
    global my_sum
    dx = [0, 1]
    dy = [1, 0]
    x = idx
    y = idy
    if idx == N-1 and idy == N-1:
        if result < my_sum:
            my_sum = result
            return
    else:
        for i in range(2):
            idx = x
            idy = y
            if idx+dx[i] < 0 or idy+dy[i] < 0 or idx+dx[i] > N - 1 or idy+dy[i] > N - 1:
                pass
            else:
                if visited[idy+dy[i]][idx+dx[i]] == 0:
                    if result + matrix[idy+dy[i]][idx+dx[i]] < my_sum:
                        idy += dy[i]
                        idx += dx[i]
                        visited[idy][idx] = 1
                        backtracking(idx, idy, result+matrix[idy][idx])
                        visited[idy][idx] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    my_sum = 1000000000000000000000
    backtracking(0, 0, matrix[0][0])
    print('#{} {}'.format(test_case, my_sum))