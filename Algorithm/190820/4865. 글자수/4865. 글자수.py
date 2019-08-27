import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    str_1 = list(input())
    str_2 = list(input())
    count_list = []
    for i in str_2:
        for j in str_1:
            if i == j:
                count_list.append(str_2.count(i))
    count_list.sort()
    print('#{} {}'.format(test_case, count_list[-1]))
