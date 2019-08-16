import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    entire_page, A_page, B_page = map(int, input().split())
    binary_num = entire_page
    right_num = entire_page
    left_num = 1
    count_A = count_B = 0
    while binary_num != A_page:
        if A_page > int((right_num + left_num)/2):
            left_num = int((right_num + left_num)/2)
        else:
            right_num = int((right_num + left_num)/2)
        binary_num = int((right_num + left_num)/2)
        count_A += 1
    binary_num = entire_page
    right_num = entire_page
    left_num = 1
    while binary_num != B_page:
        if B_page > int((right_num + left_num) / 2):
            right_num = right_num
            left_num = int((right_num + left_num) / 2)
        else:
            left_num = left_num
            right_num = int((right_num + left_num) / 2)
        binary_num = int((right_num + left_num) / 2)
        count_B += 1
    if count_A > count_B:
        print('#{} B'.format(test_case))
    elif count_A == count_B:
        print('#{} 0'.format(test_case))
    else:
        print('#{} A'.format(test_case))