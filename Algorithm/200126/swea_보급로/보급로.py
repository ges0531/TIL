import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


def search_road(start_node, visited, result):
    global my_min
    if start_node == [N-1, N-1]:
        my_min = result
        return
    for i in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < N and 0 <= idx < N:
            if not [idy, idx] in visited:
                if result+matrix[idy][idx] < my_min:
                    visited.append(start_node)
                    search_road([idy, idx], visited, result+matrix[idy][idx])
                    visited.pop()

T = int(input())
# T = 1
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    my_min = 100000
    dequeue = deque([0, 0])
    memoization = [[0] * N for _ in range(N)]
    search_road([0, 0], dequeue,  matrix[0][0])
    print(memoization)

    print('#{} {}'.format(test_case, my_min))