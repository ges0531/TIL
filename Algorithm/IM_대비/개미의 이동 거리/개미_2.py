import sys


sys.stdin = open('input.txt', 'r')


def right():
    global count, location, direction
    direction = 0
    while True:
        location[1] += 1
        count += 1
        if matrix[location[0]][location[1]] == 1:
            break
        elif matrix[location[0]][location[1]] == 2:
            break
        elif matrix[location[0]][location[1]] == 'A':
            break


def left():
    global count, location, direction
    direction = 1
    while True:
        location[1] -= 1
        count += 1
        if matrix[location[0]][location[1]] == 1:
            break
        elif matrix[location[0]][location[1]] == 2:
            break
        elif matrix[location[0]][location[1]] == 'A':
            break


def up():
    global count, location, direction
    direction = 2
    while True:
        location[0] -= 1
        count += 1
        if matrix[location[0]][location[1]] == 1:
            break
        elif matrix[location[0]][location[1]] == 2:
            break
        elif matrix[location[0]][location[1]] == 'A':
            break


def down():
    global count, location, direction
    direction = 3
    while True:
        location[0] += 1
        count += 1
        if matrix[location[0]][location[1]] == 1:
            break
        elif matrix[location[0]][location[1]] == 2:
            break
        elif matrix[location[0]][location[1]] == 'A':
            break


T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    size = size + 2
    matrix = [['A'] * size for _ in range(size)]
    for i in range(1, size - 1):
        s = list(map(int, input().split()))
        matrix[i][1:size - 1] = s[:]
    location = [1, 1]
    direction = -1
    count = 0
    right()
    while matrix[location[0]][location[1]] != 'A':
        if direction == 0:
            if matrix[location[0]][location[1]] == 1:
                up()
            elif matrix[location[0]][location[1]] == 2:
                down()
        elif direction == 1:
            if matrix[location[0]][location[1]] == 1:
                down()
            elif matrix[location[0]][location[1]] == 2:
                up()
        elif direction == 2:
            if matrix[location[0]][location[1]] == 1:
                right()
            elif matrix[location[0]][location[1]] == 2:
                left()
        elif direction == 3:
            if matrix[location[0]][location[1]] == 1:
                left()
            elif matrix[location[0]][location[1]] == 2:
                right()
    print('#{} {}'.format(test_case, count-1))