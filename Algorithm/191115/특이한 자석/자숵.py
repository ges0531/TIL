import sys

sys.stdin = open('input.txt', 'r')


def link_check(m_list):
    result_list = [0]*3
    if magnetic_list[0][2] == magnetic_list[1][6]:
        result_list[0] = 1
    if magnetic_list[1][2] == magnetic_list[2][6]:
        result_list[1] = 1
    if magnetic_list[2][2] == magnetic_list[3][6]:
        result_list[2] = 1
    return result_list




T = int(input())
T = 1
for test_case in range(1, T+1):
    rotation_count = int(input())
    magnetic_list = [list(map(int, input().split())) for _ in range(4)]
    rotation_list = [list(map(int, input().split())) for _ in range(rotation_count)]
    for i in range(len(rotation_list)):
        rotation_list[i][0] -= 1
    