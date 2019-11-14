import sys

sys.stdin = open('input.txt', 'r')


def perm(k, result):
    global my_min, my_max
    if k == number_count:
        if my_min > result:
            my_min = result
        if my_max < result:
            my_max = result
    else:
        if operator_list[0]:
            operator_list[0] -= 1
            perm(k + 1, result + number_list[k])
            operator_list[0] += 1
        if operator_list[1]:
            operator_list[1] -= 1
            perm(k + 1, result - number_list[k])
            operator_list[1] += 1
        if operator_list[2]:
            operator_list[2] -= 1
            perm(k + 1, result * number_list[k])
            operator_list[2] += 1
        if operator_list[3]:
            operator_list[3] -= 1
            perm(k + 1, int(result / number_list[k]))
            operator_list[3] += 1


T = int(input())

for test_case in range(1, T+1):
    number_count = int(input())
    operator_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    my_min = 100000001
    my_max = -100000001
    perm(1, number_list[0])
    print('#{} {}'.format(test_case, my_max-my_min))