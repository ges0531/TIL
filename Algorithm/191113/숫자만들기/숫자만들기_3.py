import sys
import itertools

sys.stdin = open('input.txt', 'r')


def calculate(result_list):
    for l in range(len(result_list)//2):
        if result_list[(2*l)+1] == '+':
            result_list[(2*l)+2] = result_list[2*l] + result_list[(2*l)+2]
        elif result_list[(2*l)+1] == '-':
            result_list[(2 * l) + 2] = result_list[2 * l] - result_list[(2 * l) + 2]
        elif result_list[(2*l)+1] == '*':
            result_list[(2 * l) + 2] = result_list[2 * l] * result_list[(2 * l) + 2]
        elif result_list[(2*l)+1] == '/':
            result_list[(2 * l) + 2] = int(result_list[2 * l] / result_list[(2 * l) + 2])
    return result_list[-1]


T = int(input())

for test_case in range(1, T+1):
    number_count = int(input())
    operator_count = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    operator = ['+', '-', '*', '/']
    operator_list = []
    my_min = 100000000
    my_max = -100000000
    for i in range(4):
        for j in range(operator_count[i]):
            operator_list.append(operator[i])
    my_list = list(set(itertools.permutations(operator_list)))
    for jj in range(len(my_list)):
        result_list = []
        for ii in range(len(operator_list)):
            result_list.append(number_list[ii])
            result_list.append(my_list[jj][ii])
        result_list.append(number_list[-1])
        result = calculate(result_list)
        if result > my_max:
            my_max = result
        if result < my_min:
            my_min = result
    print('#{} {}'.format(test_case, my_max-my_min))
