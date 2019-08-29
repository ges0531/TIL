import sys

sys.stdin = open('input.txt', 'r')

size = 10
size = size + 4
matrix = [[2]*size for _ in range(size)]
for i in range(2, size-2):
    input_data = list(map(int, input().split()))
    matrix[i][2:size-2] = input_data[:]

location = count = 0
dx = [0, 0, -1, 1, -1, 1, -1, 1, 0]
dy = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
for column in range(len(matrix)):
    for row in range(len(matrix[0])):
        if matrix[column][row] == 3:
            location = [column, row]

first = [location[0], location[1]]
while True:  # 위로
    location[0] -= 1
    print(location, 1)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
while True:  # 아래로
    location[0] += 1
    print(location, 2)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
while True:  # 오른쪽
    location[1] += 1
    print(location, 3)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
while True:  # 왼쪽
    location[1] -= 1
    print(location, 4)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
while True:  # 왼쪽 위
    location[1] -= 1
    location[0] -= 1
    print(location, 5)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
while True:  # 오른쪽 위
    location[1] += 1
    location[0] -= 1
    print(location, 6)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
while True:  # 왼쪽 아래
    location[1] -= 1
    location[0] += 1
    print(location, 7)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
while True:  # 오른쪽 아래
    location[1] += 1
    location[0] += 1
    print(location, 8)
    for cnt in range(9):
        if matrix[location[0]+dy[cnt]][location[1]+dx[cnt]] == 1:
            count += 1
            matrix[location[0] + dy[cnt]][location[1] + dx[cnt]] = 0
    if matrix[location[0]][location[1]] == 2:
        location = [first[0], first[1]]
        break
print(count)