import sys

sys.stdin = open('input.txt', 'r')

makuwa_count = int(input())
direction = [0] * 6
area = [0] * 6
matrix = [list(map(int, input().split())) for _ in range(6)]
matrix = sum(matrix, [])
for i in range(6):
    direction[i] = matrix[2*i]
    area[i] = matrix[2*i+1]
small = 0
for j in range(len(direction)):
    if direction[j] == 3:
        if direction[j-1] == 1:
            small = j
            break
    elif direction[j] == 2:
        if direction[j-1] == 3:
            small = j
            break
    elif direction[j] == 4:
        if direction[j-1] == 2:
            small = j
            break
    elif direction[j] == 1:
        if direction[j-1] == 4:
            small = j
            break
result = area[small] * area[small+1]