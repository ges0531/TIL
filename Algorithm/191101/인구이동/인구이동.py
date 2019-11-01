import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global visited
    queue = [start_node]
    visited[start_node[0]][start_node[1]] = 1
    flag = 0
    while queue:
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if people_min <= abs(country_matrix[y][x]-country_matrix[idy][idx]) <= people_max:
                        visited[idy][idx] = 1
                        queue.append([idy, idx])
                        division_count += 1
                        my_sum += country_matrix[idy][idx]
                        location_list.append([idy, idx])
                        flag = 1

    if flag:
        return True


size, people_min, people_max = map(int, input().split())
country_matrix = [list(map(int, input().split())) for _ in range(size)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 1
result = 0
while count:
    count = 0
    visited = [[0] * size for _ in range(size)]
    for row in range(len(country_matrix)):
        for column in range(len(country_matrix[row])):
            if BFS([row, column]):
                count += 1
    result += count
    print(count)
print(result)
