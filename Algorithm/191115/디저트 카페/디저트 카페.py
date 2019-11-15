import sys

sys.stdin = open('input.txt', 'r')

def DFS(start_node):
    global visited, num_list, my_max
    for i in range(4):
        idy = start_node[0]+dy[i]
        idx = start_node[1]+dx[i]
        if 0 <= idy < size and 0 <= idx < size:
            if visited[idy][idx] == 1:
                result = visited[start_node[0]][start_node[1]]
                if my_max < result:
                    my_max = result
            if not visited[idy][idx]:
                if matrix[idy][idx] not in num_list:
                    visited[idy][idx] = visited[start_node[0]][start_node[1]] + 1
                    num_list.append(matrix[idy][idx])
                    DFS([idy, idx])
                    num_list.pop()
                    visited[idy][idx] = 0
    for v in visited:
        print(v)
    print()

T = int(input())
T = 1
for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    my_max = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            num_list = []
            visited = [[0] * size for _ in range(size)]
            visited[i][j] = 1
            num_list.append(matrix[i][j])
            print('----------------------')
            DFS([i, j])
    if my_max < 4:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, my_max))
