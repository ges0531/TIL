import sys

sys.stdin = open('input.txt', 'r')

def change_direction(cur, change):
    if cur

matrix_length = int(input())
matrix = [[0]*matrix_length for _ in range(matrix_length)]
apple_count = int(input())
apple_list = [list(map(int, list(input().split()))) for _ in range(apple_count)]
direction_count = int(input())
direction_list = [list(list(input().split())) for _ in range(direction_count)]
for i in range(direction_count):
    direction_list[i][0] = int(direction_list[i][0])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
a = b = 0
snake_location = [a, b]
direction_flag = 3
while True:
    a += dy[direction_flag]
    b += dx[direction_flag]




def change_direction():

