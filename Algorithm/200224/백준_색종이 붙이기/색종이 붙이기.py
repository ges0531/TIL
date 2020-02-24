import sys

sys.stdin = open('input.txt', 'r')

matrix = [list(map(int, input().split())) for _ in range(10)]
