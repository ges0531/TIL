import sys
import time
sys.stdin = open('input.txt', 'r')
stime = time.time()
def power_set(k, n, t, arr):
    global energy, my_max
    if k == n:
        my_sum = 0
        for ii in range(len(t)):
            if t[ii]:
                my_sum += mineral_location[ii][2]
        if my_sum > my_max:
            my_max = my_sum
    else:
        t[k] = arr[k]
        if sum(t) <= energy:
            power_set(k+1, n, t, arr)
        t[k] = 0
        if sum(t) <= energy:
            power_set(k+1, n, t, arr)

T = int(input())

for test_case in range(1, T+1):
    matrix_column, matrix_row, energy = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_column)]
    mineral_location = []
    robot_location = []
    my_max = 0
    for column in range(len(matrix)):
        for row in range(len(matrix[column])):
            if matrix[column][row] == 1:
                robot_location = [column, row]
            elif matrix[column][row]:
                mineral_location.append([column, row, matrix[column][row]])
    track_sum = [0]*len(mineral_location)
    for i in range(len(mineral_location)):
        track_sum[i] = 2*(abs(robot_location[0]-mineral_location[i][0])+abs(robot_location[1]-mineral_location[i][1]))
    power_set(0, len(track_sum), [0]*len(track_sum), track_sum)
    print('#{} {}'.format(test_case, my_max))
    print(time.time() - stime)