import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size, game_count = map(int, input().split())
    size = size + 2
    matrix = [[3]*size for _ in range(size)]
    a = 0
    for i in range(1, size-1):
        s = [0] * (size-2)
        matrix[i][1:size-1] = s[:]
    start_node = (size-2)//2
    matrix[start_node][start_node] = 2
    matrix[start_node+1][start_node] = 1
    matrix[start_node][start_node+1] = 1
    matrix[start_node+1][start_node+1] = 2
    for i in range(game_count):
        location = list(map(int, input().split()))
        matrix[location[1]][location[0]] = location[2]
        if matrix[location[1]][location[0]] == 1:
            for j in range(8):
                dx = [0, 0, -1, 1, -1, 1, -1, 1]
                dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                if matrix[location[1]+dy[j]][location[0]+dx[j]] == 2:
                    while matrix[location[1]+dy[j]][location[0]+dx[j]] == 2:
                        dy[j] += dy[j]
                        dx[j] += dx[j]
                        if matrix[location[1]+dy[j]][location[0]+dx[j]] == 1:
                            a = 1
                    dx = [0, 0, -1, 1, -1, 1, -1, 1]
                    dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                    if a == 1:
                        while matrix[location[1] + dy[j]][location[0] + dx[j]] == 2:
                            matrix[location[1] + dy[j]][location[0] + dx[j]] = 1
                            dy[j] += dy[j]
                            dx[j] += dx[j]
                    dx = [0, 0, -1, 1, -1, 1, -1, 1]
                    dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                    a = 0
            print(matrix, 1)
        elif matrix[location[1]][location[0]] == 2:
            for j in range(8):
                dx = [0, 0, -1, 1, -1, 1, -1, 1]
                dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                if matrix[location[1] + dy[j]][location[0] + dx[j]] == 1:
                    while matrix[location[1] + dy[j]][location[0] + dx[j]] == 1:
                        dy[j] += dy[j]
                        dx[j] += dx[j]
                        if matrix[location[1] + dy[j]][location[0] + dx[j]] == 2:
                            a = 1
                    dx = [0, 0, -1, 1, -1, 1, -1, 1]
                    dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                    if a == 1:
                        while matrix[location[1] + dy[j]][location[0] + dx[j]] == 1:
                            matrix[location[1] + dy[j]][location[0] + dx[j]] = 2
                            dy[j] += dy[j]
                            dx[j] += dx[j]
                    dx = [0, 0, -1, 1, -1, 1, -1, 1]
                    dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                    a = 0
            print(matrix, 2)
    print(matrix)

                # elif matrix[location[1]+dy[j]][location[0]+dx[j]] == 1:
                #     while matrix[location[1]+dy[j]][location[0]+dx[j]] == 1:
                #         dy[j] += dy[j]
                #         dx[j] += dx[j]
                #         if matrix[location[1]+dy[j]][location[0]+dx[j]] == 2:
                #             a = 1
                #     dx = [0, 0, -1, 1, -1, 1, -1, 1]
                #     dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                #     if a == 1:
                #         while matrix[location[1] + dy[j]][location[0] + dx[j]] == 1:
                #             dy[j] += dy[j]
                #             dx[j] += dx[j]
                #             matrix[location[1] + dy[j]][location[0] + dx[j]] = 2
                #     dx = [0, 0, -1, 1, -1, 1, -1, 1]
                #     dy = [-1, 1, 0, 0, -1, 1, -1, 1]
                #     a = 0