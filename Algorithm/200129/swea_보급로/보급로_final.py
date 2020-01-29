import sys

sys.stdin = open('input.txt', 'r')


def search_road(start_node, result):
    global my_min
    if start_node == [N-1, N-1]:
        if my_min == 0:
            my_min = result
        else:
            if my_min > result:
                my_min = result
        return
    if 0 < my_min < result:
        return
    if memoization[start_node[0]][start_node[1]] == 0:
        memoization[start_node[0]][start_node[1]] = result
    else:
        if memoization[start_node[0]][start_node[1]] > result:
            memoization[start_node[0]][start_node[1]] = result
        else:
            return
    for i in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < N and 0 <= idx < N:
            if not visited[idy][idx]:
                visited[idy][idx] = 1
                search_road([idy, idx], result+matrix[idy][idx])
                visited[idy][idx] = 0

T = int(input())
# T = 3
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    my_min = 0
    memoization = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    search_road([0, 0],  matrix[0][0])

    # for m in memoization:
    #     print(m)
    print('#{} {}'.format(test_case, my_min))