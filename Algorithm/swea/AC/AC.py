import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    function_list = list(input())
    number_count = int(input())
    number_list = input()[1:-1].split(',')
    my_list = []
    count = 0
    for i in range(len(function_list)):
        if function_list[i] == 'R':
            count += 1
        else:
            if count % 2:
                my_list.append('R')
            my_list.append('D')
            count = 0
    for j in range(len(my_list)):
        if number_list:
            if my_list[j] == 'R':
                number_list.reverse()
            elif my_list[j] == 'D':
                number_list.pop(0)
    if number_list:
        print('[', end='')
        print(','.join(number_list), end='')
        print(']')
    else:
        print('error')
