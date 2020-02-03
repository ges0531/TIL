import sys

sys.stdin = open('input.txt', 'r')


def snake(start_node, count, snake_direction, snake_list):
    if not (0 <= start_node[0] < matrix_size and 0 <= start_node[1] < matrix_size):
        print(count)
        return
    if matrix[start_node[0]][start_node[1]] == 2:
        print(count)
        return
    if matrix[start_node[0]][start_node[1]] == 1:
        snake_list.append([start_node[0], start_node[1]])
        matrix[start_node[0]][start_node[1]] = 2
    else:
        snake_list.append([start_node[0], start_node[1]])
        matrix[start_node[0]][start_node[1]] = 2
        pop_flag = snake_list.pop(0)
        matrix[pop_flag[0]][pop_flag[1]] = 0
    if str(count) in direction_dict:
        if direction_dict[str(count)] == 'D':
            snake_direction = (snake_direction+1) % 4
        else:
            snake_direction = (snake_direction+3) % 4
    snake([start_node[0]+dy[snake_direction], start_node[1]+dx[snake_direction]], count+1, snake_direction, snake_list)


matrix_size = int(input())
matrix = [[0]*matrix_size for _ in range(matrix_size)]
matrix[0][0] = 1
apple_count = int(input())
apple_location = [list(map(int, input().split())) for _ in range(apple_count)]
for i in range(apple_count):
    matrix[apple_location[i][0]-1][apple_location[i][1]-1] = 1
direction_count = int(input())
direction_list = [list(input().split()) for _ in range(direction_count)]
direction_dict = {direction_list[j][0]: direction_list[j][1] for j in range(len(direction_list))}
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
snake([0, 0], 0, 1, [])
