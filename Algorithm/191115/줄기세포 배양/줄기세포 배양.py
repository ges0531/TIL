import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
T = 1
for test_case in range(1, T+1):
    matrix_row, matrix_column, breeding_time = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_row)]