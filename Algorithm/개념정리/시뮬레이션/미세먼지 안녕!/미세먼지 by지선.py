import sys

sys.stdin = open('input.txt', 'r')

def is_wall(x, y):
    return 0 <= x < R and 0 <= y < C

def air(lst):
    global total_mg
    total_mg -= lst[air_index[0]-1][0]  #위 쪽 회전
    lst[air_index[0] - 1][0] = 0
    move_x = air_index[0]-1
    move_y = 0
    while move_x != 0:
        lst[move_x][0] = lst[move_x-1][0]
        move_x -= 1
    while move_y != C-1:
        lst[0][move_y] = lst[0][move_y+1]
        move_y += 1
    while move_x != air_index[0]:
        lst[move_x][C-1] = lst[move_x+1][C-1]
        move_x += 1
    while move_y != 0:
        lst[air_index[0]][move_y] = lst[air_index[0]][move_y-1]
        move_y -= 1
    total_mg -= lst[air_index[2]+1][0]  # 아래 쪽 회전
    lst[air_index[2] + 1][0] = 0
    move_x = air_index[0]+1
    move_y = 0
    while move_x != R-1:
        lst[move_x][0] = lst[move_x+1][0]
        move_x += 1
    while move_y != C - 1:
        lst[R-1][move_y] = lst[R-1][move_y + 1]
        move_y += 1
    while move_x != air_index[2]:
        lst[move_x][C-1] = lst[move_x-1][C - 1]
        move_x -= 1
    while move_y != 0:
        lst[air_index[2]][move_y] = lst[air_index[2]][move_y-1]
        move_y -= 1

R, C, T = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(R)]

total_mg = 0
air_index = []
for i in range(R):
    for j in range(C):
        if info[i][j] == -1:
            air_index += [i, j]
        elif info[i][j] > 0:
            total_mg += info[i][j]
time = 0
while time != T:  # 먼지 확산
    time += 1
    new_mg = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if info[i][j] > 0:
                cnt = 0
                for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
                    if is_wall(i+x, j+y) and info[i+x][j+y] != -1:
                        cnt += 1
                        new_mg[i+x][j+y] += info[i][j]//5
                new_mg[i][j] += (info[i][j] - (info[i][j]//5)*cnt)
    air(new_mg)
    new_mg[air_index[0]][air_index[1]] = new_mg[air_index[2]][air_index[3]] = -1
    for i in range(R):
        for j in range(C):
            info[i][j] = new_mg[i][j]
for v in info:
    print(v)
print(total_mg)