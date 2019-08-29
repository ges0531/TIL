import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    location = [0] * len(atom)
    direction = [0] * len(atom)
    energy = [0] * len(atom)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(len(atom)):
        location[i] = [atom[i][0], atom[i][1]]
        direction[i] = atom[i][2]
        energy[i] = atom[i][3]

    matrix = [[0]*4000 for _ in range(4000)]
    for loca in location:
        matrix[2000+loca[0]][2000+loca[1]] = 2
    my_sum = 0

    for column in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[column][row] == 2:
                if direction[location.index([column-2000, row-2000])] == 0:
                    if direction[location.index([column - 2000, row - 2001])] == 1:
                        matrix[column][row] = 0
                        matrix[column][row - 1] = 0
                        my_sum += energy[location.index([column - 2000, row - 2001])]
                    elif direction[location.index([column - 2000, row - 2002])] == 1:
                        matrix[column][row] = 0
                        matrix[column][row - 2] = 0
                        my_sum += energy[location.index([column - 2000, row - 2002])]
                    elif direction[location.index([column - 1999, row - 2001])] == 2:
                        matrix[column][row] = 0
                        matrix[column+1][row - 1] = 0
                        my_sum += energy[location.index([column - 1999, row - 2001])]
                    elif direction[location.index([column - 2001, row - 2001])] == 3:
                        matrix[column][row] = 0
                        matrix[column-1][row - 1] = 0
                        my_sum += energy[location.index([column - 2001, row - 2001])]
                    else:
                        matrix[column][row] = 0
                        matrix[column][row - 1] = 2
                elif direction[location.index([column-2000, row-2000])] == 1:
                    if direction[location.index([column - 2000, row - 1999])] == 0:
                        matrix[column][row] = 0
                        matrix[column][row + 1] = 0
                        my_sum += energy[location.index([column - 2000, row - 1999])]
                    elif direction[location.index([column - 2000, row - 1998])] == 0:
                        matrix[column][row] = 0
                        matrix[column][row + 2] = 0
                        my_sum += energy[location.index([column - 2000, row - 1998])]
                    elif direction[location.index([column - 1999, row - 1999])] == 2:
                        matrix[column][row] = 0
                        matrix[column+1][row + 1] = 0
                        my_sum += energy[location.index([column - 1999, row - 1999])]
                    elif direction[location.index([column - 2001, row - 1999])] == 3:
                        matrix[column][row] = 0
                        matrix[column-1][row + 1] = 0
                        my_sum += energy[location.index([column - 2001, row - 1999])]
                    else:
                        matrix[column][row] = 0
                        matrix[column][row - 1] = 2
                elif direction[location.index([column-2000, row-2000])] == 2:
                    if direction[location.index([column - 2001, row - 2000])] == 3:
                        matrix[column][row] = 0
                        matrix[column-1][row] = 0
                        my_sum += energy[location.index([column - 2001, row - 2000])]
                    elif direction[location.index([column - 2002, row - 2000])] == 3:
                        matrix[column][row] = 0
                        matrix[column-2][row] = 0
                        my_sum += energy[location.index([column - 2002, row - 2000])]
                    elif direction[location.index([column - 2001, row - 2001])] == 0:
                        matrix[column][row] = 0
                        matrix[column-1][row-1] = 0
                        my_sum += energy[location.index([column - 2001, row - 2001])]
                    elif direction[location.index([column - 2001, row - 1999])] == 1:
                        matrix[column][row] = 0
                        matrix[column-1][row + 1] = 0
                        my_sum += energy[location.index([column - 2001, row - 1999])]
                    else:
                        matrix[column][row] = 0
                        matrix[column][row - 1] = 2
                elif direction[location.index([column-2000, row-2000])] == 3:
                    if direction[location.index([column - 1999, row - 2000])] == 2:
                        matrix[column][row] = 0
                        matrix[column+1][row] = 0
                        my_sum += energy[location.index([column - 1999, row - 2000])]
                    elif direction[location.index([column - 1998, row - 2000])] == 2:
                        matrix[column][row] = 0
                        matrix[column+2][row] = 0
                        my_sum += energy[location.index([column - 1998, row - 2000])]
                    elif direction[location.index([column - 1999, row - 1999])] == 0:
                        matrix[column][row] = 0
                        matrix[column-1][row-1] = 0
                        my_sum += energy[location.index([column - 1999, row - 1999])]
                    elif direction[location.index([column - 1999, row - 2001])] == 1:
                        matrix[column][row] = 0
                        matrix[column-1][row + 1] = 0
                        my_sum += energy[location.index([column - 1999, row - 2001])]
                    else:
                        matrix[column][row] = 0
                        matrix[column][row - 1] = 2
    print(my_sum)


