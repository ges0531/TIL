def bfs(R, C, dirs, L):
    global visit

    q = [(R, C, dirs)]
    visit += 1
    arr[R][C] = 0

    for _ in range(L - 1):
        for _ in range(len(q)):
            y, x, dirs = q.pop(0)
            for dir in dirs:
                if dir == 1:
                    if 0 <= y - 1 < N and arr[y - 1][x]:
                        if 3 in arr[y - 1][x]:
                            q.append((y - 1, x, arr[y - 1][x]))
                            visit += 1
                            arr[y - 1][x] = 0
                elif dir == 2:
                    if 0 <= x + 1 < M and arr[y][x + 1]:
                        if 4 in arr[y][x + 1]:
                            q.append((y, x + 1, arr[y][x + 1]))
                            visit += 1
                            arr[y][x + 1] = 0
                elif dir == 3:
                    if 0 <= y + 1 < N and arr[y + 1][x]:
                        if 1 in arr[y + 1][x]:
                            q.append((y + 1, x, arr[y + 1][x]))
                            visit += 1
                            arr[y + 1][x] = 0
                elif dir == 4:
                    if 0 <= x - 1 < M and arr[y][x - 1]:
                        if 2 in arr[y][x - 1]:
                            q.append((y, x - 1, arr[y][x - 1]))
                            visit += 1
                            arr[y][x - 1] = 0
        if not q:
            break


for tc in range(1, 1 + int(input())):
    N, M, R, C, L = map(int, input().split())  # L: 탈출 후 소요시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                if arr[i][j] == 1:
                    arr[i][j] = (1, 2, 3, 4)
                elif arr[i][j] == 2:
                    arr[i][j] = (1, 3)
                elif arr[i][j] == 3:
                    arr[i][j] = (2, 4)
                elif arr[i][j] == 4:
                    arr[i][j] = (1, 2)
                elif arr[i][j] == 5:
                    arr[i][j] = (2, 3)
                elif arr[i][j] == 6:
                    arr[i][j] = (3, 4)
                elif arr[i][j] == 7:
                    arr[i][j] = (4, 1)

    visit = 0
    bfs(R, C, arr[R][C], L)
    print('#%d %d' % (tc, visit))