import sys

sys.stdin = open('input.txt', 'r')

def DFS(start_node, direction_count, result):
    global my_max
    if direction_count == 3:
        if my_max < result:
            my_max = result
    elif start_node[0] < 0 or start_node[0] >= size or start_node[1] < 0 or start_node[1] >= size:
        return
    elif matrix[start_node[0]][start_node[1]] in number_list:
        return
    else:
        if direction_count == 0:
            DFS([start_node[0]+dy[direction_count], start_node[1]+dx[direction_count]])



T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    my_max = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            number_list = []
            number_list.append(matrix[i][j])
            DFS([i, j], 0, 0)

        print('#{} {}'.format(test_case, my_max))