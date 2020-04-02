import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global visited, my_list, my_sum, my_count, flag
    queue = [start_node]
    visited[start_node[0]][start_node[1]] = 1
    while queue:
        a = queue.pop(0)
        my_list.append(a)
        my_sum += country_matrix[a[0]][a[1]]
        my_count += 1
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if people_min <= abs(country_matrix[y][x]-country_matrix[idy][idx]) <= people_max:
                        visited[idy][idx] = visited[y][x]
                        queue.append([idy, idx])
                        flag += 1


size, people_min, people_max = map(int, input().split())
country_matrix = [list(map(int, input().split())) for _ in range(size)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0
flag = 1
while flag:
    flag = 0
    visited = [[0] * size for _ in range(size)]
    for row in range(len(country_matrix)):
        for column in range(len(country_matrix[row])):
            if not visited[row][column]:
                my_list = []
                my_sum = 0
                my_count = 0
                BFS([row, column])
                for j in range(len(my_list)):
                    country_matrix[my_list[j][0]][my_list[j][1]] = my_sum//my_count
    count += 1
print(count-1)
