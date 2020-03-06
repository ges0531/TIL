import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node):
    global shark_count, shark, result
    queue = [start_node]
    visited = [[0]*size for _ in range(size)]
    visited[start_node[0]][start_node[1]] = 1
    my_location = []
    my_min = 10000000000
    while queue:
        # if my_location:
        #     break
        a = queue.pop(0)
        for i in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[i]
            idx = x+dx[i]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if shark_count == shark:
                        shark += 1
                        shark_count = 0
                    if shark >= matrix[idy][idx]:
                        visited[idy][idx] = visited[y][x]+1
                        queue.append([idy, idx])
                    if shark > matrix[idy][idx] and matrix[idy][idx]:
                        if my_min >= visited[idy][idx]:
                            my_min = visited[idy][idx]
                            my_location.append([idy, idx])

    if my_location:
        for col_1 in range(len(matrix)):
            for row_1 in range(len(matrix[col_1])):
                if visited[col_1][row_1] == my_min and [col_1, row_1] in my_location:
                    result += visited[col_1][row_1] - 1
                    return [col_1, row_1]


size = int(input())

matrix = [list(map(int, input().split())) for _ in range(size)]
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
count = 0
result = 0
shark_count = 0
shark = 2
for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        if matrix[column][row] == 9:
            shark_location = [column, row]
            matrix[column][row] = 0
        elif matrix[column][row]:
            count += 1

for _ in range(count):
    my_list = BFS(shark_location)

    if my_list:
        matrix[my_list[0]][my_list[1]] = 0
        shark_count += 1
        shark_location = my_list
print(result)
