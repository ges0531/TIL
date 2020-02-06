import sys

sys.stdin = open('input.txt', 'r')

import sys
sys.setrecursionlimit(1000000)
def move_robot(start_node, robot_dir, count):
    global result
    if count == 4 and not (0 <= start_node[0]+dy[(robot_dir+2)%4] < matrix_column and 0 <= start_node[1]+dx[(robot_dir+2)%4] < matrix_row):
        return
    # if count == 4 and matrix[start_node[0]+dy[(robot_dir+2)%4]][start_node[1]+dx[(robot_dir+2)%4]]:
    #     return
    if not matrix[start_node[0]][start_node[1]]:
        matrix[start_node[0]][start_node[1]] = 2
        result += 1
    if count == 4:
        move_robot([start_node[0]+dy[(robot_dir+2)%4], start_node[1]+dx[(robot_dir+2)%4]], robot_dir, 0)
    elif not (0 <= start_node[0]+dy[(robot_dir+3)%4] < matrix_column and 0 <= start_node[1]+dx[(robot_dir+3)%4] < matrix_row):
        move_robot(start_node, (robot_dir+3)%4, count+1)
    elif matrix[start_node[0]+dy[(robot_dir+3)%4]][start_node[1]+dx[(robot_dir+3)%4]]:
        move_robot(start_node, (robot_dir+3) % 4, count+1)
    else:
        move_robot([start_node[0]+dy[(robot_dir+3)%4], start_node[1]+dx[(robot_dir+3)%4]], (robot_dir+3) % 4, 0)


matrix_column, matrix_row = map(int, input().split())
robot_location = list(map(int, input().split()))
robot_direction = robot_location.pop()
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
result = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
move_robot(robot_location, robot_direction, 0)
print(result)
