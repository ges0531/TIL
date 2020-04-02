import sys

sys.stdin = open('input.txt', 'r')

def backtracking(result, idx, idy, count):
    global min_result

    dx = [1, 0]
    dy = [0, 1]
    x = idx
    y = idy

    # if count > 2*N-1:
    #     return

    if idx == N-1 and idy == N-1:

        if result < min_result:
            min_result = result
        return

    else:
        for i in range(2):
            idx = x
            idy = y
            idx = idx + dx[i]
            idy = idy + dy[i]

            if idx < 0 or idy < 0 or idx > N - 1 or idy > N - 1:
                pass
            else:
                if not visited[idx][idy]:
                    if result+board[idx][idy] < min_result:
                        visited[idx][idy] = 1
                        backtracking(result+board[idx][idy], idx, idy, count+1)
                        visited[idx][idy] = 0



T = int(input())

for tc in range(1, T+1):

    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    x = y = 0
    min_result = 1000000000000000000
    result = board[0][0]
    count = 1
    backtracking(result, x, y, count)
    print('#{} {}'.format(tc, min_result))