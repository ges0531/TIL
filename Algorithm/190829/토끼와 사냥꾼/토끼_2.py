import sys


sys.stdin = open('input.txt', 'r')

size = 10
size = size + 2
matrix = [[2]*size for _ in range(size)]
count = 0
loca = []
for i in range(1, size-1):
    input_data = list(map(int, input().split()))
    matrix[i][1:size-1] = input_data[:]
for column in range(len(matrix)):
    for row in range(len(matrix[0])):
        if matrix[column][row] == 3:
            loca.append([column, row])
for i in range(len(loca)):
    location = loca[i]
    first = [location[0], location[1]]
    while True:  # 위로
        location[0] -= 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
    while True:  # 아래로
        location[0] += 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
    while True:  # 오른쪽
        location[1] += 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
    while True:  # 왼쪽
        location[1] -= 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
    while True:  # 왼쪽 위
        location[1] -= 1
        location[0] -= 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
    while True:  # 오른쪽 위
        location[1] += 1
        location[0] -= 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
    while True:  # 왼쪽 아래
        location[1] -= 1
        location[0] += 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
    while True:  # 오른쪽 아래
        location[1] += 1
        location[0] += 1
        if matrix[location[0]][location[1]] == 1:
            count += 1
            matrix[location[0]][location[1]] = 0
        elif matrix[location[0]][location[1]] == 2:
            location = [first[0], first[1]]
            break
print(count)