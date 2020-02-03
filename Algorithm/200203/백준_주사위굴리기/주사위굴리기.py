import sys

sys.stdin = open('input.txt', 'r')


def east(right, down, left, up):
    global dice_right, dice_down, dice_up, dice_left
    dice_right = up
    dice_down = right
    dice_left = down
    dice_up = left


def west(right, down, left, up):
    global dice_right, dice_down, dice_up, dice_left
    dice_right = down
    dice_down = left
    dice_left = up
    dice_up = right


def north(front, down, back, up):
    global dice_front, dice_down, dice_up, dice_back
    dice_front = up
    dice_down = front
    dice_back = down
    dice_up = back


def south(front, down, back, up):
    global dice_front, dice_down, dice_up, dice_back
    dice_front = down
    dice_down = back
    dice_back = up
    dice_up = front


matrix_column, matrix_row, location_y, location_x, action_count = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
action_list = list(map(int, input().split()))
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
dice_up = dice_down = dice_right = dice_left = dice_front = dice_back =  0
for i in range(action_count):
    y = location_y
    x = location_x
    idy = y+dy[action_list[i]-1]
    idx = x+dx[action_list[i]-1]
    if 0 <= idy < matrix_column and 0 <= idx < matrix_row:
        location_y = idy
        location_x = idx
        if action_list[i] == 1:
            east(dice_right, dice_down, dice_left, dice_up)
        elif action_list[i] == 2:
            west(dice_right, dice_down, dice_left, dice_up)
        elif action_list[i] == 3:
            north(dice_front, dice_down, dice_back, dice_up)
        elif action_list[i] == 4:
            south(dice_front, dice_down, dice_back, dice_up)
        if matrix[location_y][location_x] == 0:
            matrix[location_y][location_x] = dice_down
        else:
            dice_down = matrix[location_y][location_x]
            matrix[location_y][location_x] = 0
        print(dice_up)


