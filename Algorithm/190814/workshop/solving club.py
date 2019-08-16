import sys


sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T + 1):
    my_list = []
    my_box = []
    test = int(input())
    for _ in range(1, 101):
        matrix = list(map(int, input().split()))
        my_list.append(matrix)
    for row in range(len(my_list)):
        my_sum = 0
        for column in range(len(my_list[row])):
            my_sum += my_list[row][column]
        my_box.append(my_sum)
    for column in range(len(my_list[0])):
        my_sum = 0
        for row in range(len(my_list)):
            my_sum += my_list[row][column]
        my_box.append(my_sum)
    for row in range(len(my_list)):
        my_sum = 0
        for column in range(len(my_list[row])):
            if row == column:
                my_sum += my_list[row][column]
        my_box.append(my_sum)
    for row in range(len(my_list)):
        my_sum = 0
        for column in range(len(my_list[row])):
            if row + column == 99:
                my_sum += my_list[row][column]
        my_box.append(my_sum)
    print('#{} {}'.format(test_case, max(my_box)))


