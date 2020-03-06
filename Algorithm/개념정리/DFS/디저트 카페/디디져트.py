import sys

sys.stdin = open('input.txt', 'r')


def DFS(start_node, direction, direction_result):
    global visited, num_list, my_max
    for k in range(4):
        idy = start_node[0]+dy[k]
        idx = start_node[1]+dx[k]
        if 0 <= idy < size and 0 <= idx < size:
            if k == 0:
                if visited[idy][idx] == 1:
                    result = visited[start_node[0]][start_node[1]]
                    if my_max < result:
                        my_max = result
            if not visited[idy][idx]:
                if matrix[idy][idx] not in num_list:
                    if direction_result > 0:
                        visited[idy][idx] = visited[start_node[0]][start_node[1]] + 1
                        num_list.append(matrix[idy][idx])
                        if direction != k:
                            DFS([idy, idx], k, direction_result-1)
                        else:
                            DFS([idy, idx], k, direction_result)
                        num_list.pop()
                        visited[idy][idx] = 0
    # for v in visited:
    #     print(v)
    # print()


T = int(input())
# T = 2
for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    my_max = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            visited = [[0] * size for _ in range(size)]
            visited[i][j] = 1
            num_list = []
            num_list.append(matrix[i][j])
            # print('----------------------')
            for ii in range(4):
                DFS([i, j], ii, 3)

    if my_max < 4:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, my_max))
