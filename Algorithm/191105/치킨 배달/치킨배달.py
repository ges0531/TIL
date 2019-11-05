import sys
import collections

sys.stdin = open('input.txt', 'r')


def BFS(start_node, chicken):
    queue = collections.deque()
    queue.append(start_node)
    visited = [[0]*size for _ in range(size)]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.popleft()
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    visited[idy][idx] = visited[y][x]+1
                    queue.append([idy, idx])
                    if [idy, idx] in chicken:
                        return visited[idy][idx] - 1


def comb(n, r, arr, t):
    global my_min
    if r == 0:
        my_sum = 0
        for k in range(len(one_list)):
            my_sum += BFS(one_list[k], t)
        if my_min > my_sum:
            my_min = my_sum
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n-1, r, arr, t)

size, chicken_count = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(size)]
one_list = []
chicken_list = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
my_min = 10000000000
for row in range(size):
    for column in range(size):
        if matrix[row][column] == 1:
            one_list.append([row, column])
        elif matrix[row][column] == 2:
            chicken_list.append([row, column])

comb(len(chicken_list), chicken_count, chicken_list, [0]*chicken_count)
print(my_min)