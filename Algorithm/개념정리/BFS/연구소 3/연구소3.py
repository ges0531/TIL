import sys

sys.stdin = open('input.txt')


def BFS(start_list):
    global my_min, count
    my_max = 0
    virus_count = 0
    queue = []
    visited = [[0]*size for _ in range(size)]
    for i in range(len(start_list)):
        queue.append(start_list[i])
        visited[start_list[i][0]][start_list[i][1]] = 1
    while queue:
        a = queue.pop(0)
        for j in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[j]
            idx = x+dx[j]
            if 0 <= idy < size and 0 <= idx < size:
                if not visited[idy][idx]:
                    if not lab_matrix[idy][idx]:
                        visited[idy][idx] = visited[y][x]+1
                        virus_count += 1
                        queue.append([idy, idx])
                        if my_max < visited[idy][idx]:
                            my_max = visited[idy][idx]
                    elif lab_matrix[idy][idx] == 2:
                        visited[idy][idx] = visited[y][x]+1
                        queue.append([idy, idx])
    if virus_count == count:
        if my_max < my_min:
            my_min = my_max


def comb(n, r, arr, t):
    if r == 0:
        BFS(t)
    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n-1, r, arr, t)


size, virus = map(int, input().split())

lab_matrix = [list(map(int, input().split())) for _ in range(size)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
virus_list = []
my_min = 100000000
count = 0
for column in range(len(lab_matrix)):
    for row in range(len(lab_matrix[column])):
        if lab_matrix[column][row] == 2:
            virus_list.append([column, row])
        elif lab_matrix[column][row] == 0:
            count += 1
comb(len(virus_list), virus, virus_list, [0]*virus)
if my_min == 100000000:
    print(-1)
elif my_min == 0:
    print(0)
else:
    print(my_min-1)