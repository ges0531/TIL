import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    node_count = int(input())
    search = [[0, 0, 0] for _ in range(node_count)]
