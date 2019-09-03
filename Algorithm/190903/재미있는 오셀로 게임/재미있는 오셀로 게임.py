import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size, game_count = map(int, input().split())
    size = size + 2
    matrix = [[3]*size for _ in range(size)]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]
    for i in range(1, size-1):
        s = [0] * (size-2)
        matrix[i][1:size-1] = s[:]
    for i in range(game_count):
        location = list(map(int, input().split()))
        matrix[location[1]][location[0]] = location[2]
        for j in range(8):
            a = 0
            b = 0
            if matrix[location[1]][location[0]] == 1 and matrix[location[1]+dy[j]][location[0]+dx[j]] == 2:
                a += dy[j]
                b += dx[j]
                while matrix[location[1]+a][location[0]+b] == 2:
                    a += dy[j]
                    b += dx[j]
                    if matrix[location[1]+a][location[0]+b] == 1:
                        win = 1

