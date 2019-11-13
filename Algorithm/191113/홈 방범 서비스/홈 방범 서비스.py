import sys

sys.stdin = open('input.txt', 'r')


def make_k(k):
    a = 0
    k_list = [[0] * (2 * k - 1) for _ in range(2 * k - 1)]
    for k_row in range(len(k_list)):
        if k_row < len(k_list) // 2:
            for i in range(-a, a + 1):
                k_list[k_row][(len(k_list) // 2) + i] = 1
            a += 1
        else:
            for i in range(-a, a + 1):
                k_list[k_row][(len(k_list) // 2) + i] = 1
            a -= 1
    return k_list

T = int(input())
T = 1
for test_case in range(1, T+1):
    size, home_cost = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    while True:
        
