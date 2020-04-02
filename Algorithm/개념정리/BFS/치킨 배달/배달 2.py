import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')

size, chicken_count = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(size)]
one_list = []
chicken_list = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
my_min = 10000000000
my_result = 0
for row in range(size):
    for column in range(size):
        if matrix[row][column] == 1:
            one_list.append([row, column])
        elif matrix[row][column] == 2:
            chicken_list.append([row, column])
for k in list(combinations(chicken_list, chicken_count)):
    my_sum = 0
    for kkk in one_list:
        temp = 10000000000
        for kk in k:
            my_result = (abs(kk[0] - kkk[0]) + abs(kk[1]-kkk[1]))
            if my_result < temp:
                temp = my_result
        my_sum += temp
    if my_min > my_sum:
        my_min = my_sum
print(my_min)