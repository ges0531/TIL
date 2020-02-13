import sys

sys.stdin = open('input.txt', 'r')


def search_home(start_node):
    global count
    for i in range(4):
        y = start_node[0]
        x = start_node[1]
        idy = y+dy[i]
        idx = x+dx[i]
        if 0 <= idy < matrix_size and 0 <= idx < matrix_size:
            if not visited[idy][idx]:
                if matrix[idy][idx]:
                    count += 1
                    visited[idy][idx] = 1
                    search_home([idy, idx])
    return count


matrix_size = int(input())
matrix = [list(map(int, input())) for _ in range(matrix_size)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[0]*matrix_size for _ in range(matrix_size)]
visited_2 = [[0]*matrix_size for _ in range(matrix_size)]
result = []
home_count = 0
for column in range(matrix_size):
    for row in range(matrix_size):
        if matrix[column][row]:
            if not visited[column][row]:
                count = 0
                home_count += 1
                visited[column][row] = 1
                result.append(search_home([column, row]))
print(home_count)
result.sort()
for re in result:
    print(re+1)


