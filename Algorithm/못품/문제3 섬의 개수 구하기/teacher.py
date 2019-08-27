dx = [0, 1, 0, -1, -1, 1, -1, 1]
dy = [1, 0, -1, 0, 1, 1, 0, 0]


def dfs(x, y):
    if not(0 <= x < N and 0 <= y < N): return
    if not mat[x][y]: return

    mat[x][y] = 0

    for i in range(8):
        dfs(x + dx[i], y + dy[i])