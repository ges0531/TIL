import sys

sys.stdin = open('input.txt', 'r')
matrix_row, matrix_column = map(int, input().split())
robot_location = list(map(int, input().split()))
a = robot_location[0]
b = robot_location[1]
matrix = [list(map(int, input().split())) for _ in range(matrix_row)]
count = 0
while True:
    if not matrix[a][b]:
        count += 1
        matrix[a][b] = 1
    else:
        for i in range(4):
            if robot_location[2] == 0:
                if not matrix[a][b-1]:
                    b -= 1
                    robot_location[2] = 3
                    break
            elif robot_location[2] == 1:
                if not matrix[a-1][b]:
                    a -= 1
                    robot_location[2] = 0
                    break
            elif robot_location[2] == 2:
                if not matrix[a][b+1]:
                    b += 1
                    robot_location[2] = 1
                    break
            elif robot_location[2] == 3:
                if not matrix[a + 1][b]:
                    a += 1
                    robot_location[2] = 2
                    break
        else:
            if robot_location[2] == 0:
                b += 1
            elif robot_location[2] == 1:
                a += 1
            elif robot_location[2] == 2:
                b -= 1
            elif robot_location[2] == 3:
                a -= 1
