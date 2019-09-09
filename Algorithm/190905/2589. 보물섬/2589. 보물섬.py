import sys

sys.stdin = open('input.txt', 'r')


def short_track(start_node):
    global my_real_max
    queue = [start_node]
    visited = [[0]*map_row for _ in range(map_column)]
    visited[start_node[0]][start_node[1]] = 1
    location = []
    end_location = [0]
    my_real_max = 0
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < map_column and 0 <= idx < map_row:
                if visited[idy][idx] == 0:
                    if map_location[idy][idx] == 'L':
                        visited[idy][idx] = visited[y][x] + 1
                        queue.append([idy, idx])
                        my_max = visited[idy][idx]
    for column_1 in range(len(visited)):
        for row_1 in range(len(visited[0])):
            if visited[column_1][row_1] == my_max:
                location.append([column_1, row_1])

    if my_max > my_real_max:
        my_real_max = my_max
    # if len(location) == 1:
    #     return location
    # else:
    #     for j in range(len(location)-1):
    #         if abs(start_node[0]-location[j][0]) + abs(start_node[1]-location[j][1]) < abs(start_node[0]-location[j+1][0]) + abs(start_node[1]-location[j+1][1]):
    #             end_location[0] = [location[j][0], location[j][1]]
    #         else:
    #             end_location[0] = [location[j+1][0], location[j+1][1]]
    #     return end_location




T = 1

for test_case in range(1, T+1):
    map_column, map_row = list(map(int, input().split()))
    map_location = [list(input()) for _ in range(map_column)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = [0]
    for column_2 in range(len(map_location)):
        for row_2 in range(len(map_location)):
            result = short_track([column_2, row_2])
    print(my_real_max-1)
