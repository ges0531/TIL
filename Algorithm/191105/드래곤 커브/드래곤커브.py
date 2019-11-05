import sys

sys.stdin = open('input.txt', 'r')


def dragon_curve(dragon, generation):
    count = 0
    if dragon[1] == 4:
        dragon[1] = 0
    while count != generation-1:
        my_list = dragon[:]
        for i in range(len(dragon) // 2):
            if my_list[i] == 0:
                my_list[i] = 2
            elif my_list[i] == 1:
                my_list[i] = 3
            elif my_list[i] == 2:
                my_list[i] = 0
            elif my_list[i] == 3:
                my_list[i] = 1
        dragon = dragon + my_list
        count += 1
    return dragon


def dragon_location(start_node, dragon_direction):
    global visited
    y = start_node[1]
    x = start_node[0]
    visited[y][x] = 1
    for j in dragon_direction:
        y = y+dy[j]
        x = x+dx[j]
        visited[y][x] = 1


dragon_count = int(input())

dragon_list = [list(map(int, input().split())) for _ in range(dragon_count)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
visited = [[0] * 101 for _ in range(101)]
result = 0
for dragon_c in range(len(dragon_list)):
    if dragon_list[dragon_c][3]:
        dragon_location([dragon_list[dragon_c][0], dragon_list[dragon_c][1]], dragon_curve([dragon_list[dragon_c][2], dragon_list[dragon_c][2]+1], dragon_list[dragon_c][3]))
    else:
        dragon_location([dragon_list[dragon_c][0], dragon_list[dragon_c][1]], [dragon_list[dragon_c][2]])
for row in range(len(visited)-1):
    for column in range(len(visited[row])-1):
        if visited[row][column] and visited[row+1][column] and visited[row][column+1] and visited[row+1][column+1]:
            result += 1
print(result)