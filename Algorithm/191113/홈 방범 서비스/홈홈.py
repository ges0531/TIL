import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global visited
    queue = [start_node]
    count = 0
    while queue:
        a = queue.pop(0)
        for dxdy in (0, -1), (0, 1), (-1, 0), (1, 0):
            y = a[0]
            x = a[1]
            idy = y+dxdy[0]
            idx = x+dxdy[1]
            if 0 <= idy < size and 0 <= idx < size:
                if visited[idy][idx] == 1:
                    visited[idy][idx] = 2
                    queue.append([idy, idx])
                    if matrix[idy][idx]:
                        count += 1
    return count


def make_k(start_node, k):
    global visited
    a = k
    b = 0
    for j in range(k):
        for i in range(-a+1, a):
            if 0 <= start_node[0]+b < size and 0 <= start_node[1]+i < size:
                visited[start_node[0]+b][start_node[1]+i] = 1
            if 0 <= start_node[0] - b < size and 0 <= start_node[1] + i < size:
                visited[start_node[0]-b][start_node[1]+i] = 1
        a -= 1
        b += 1


T = int(input())
for test_case in range(1, T + 1):
    size, home_cost = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    k = 1
    my_max = 0
    while k <= size+2:
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                visited = [[0] * size for _ in range(size)]
                make_k([row, column], k)
                result = BFS([row, column])
                if (home_cost*result) - ((k**2)+(k-1)**2) >= 0:
                    if my_max < result:
                        my_max = result
        k += 1
    print('#{} {}'.format(test_case, my_max))


