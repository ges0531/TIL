import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    relation_count = int(input())
    friends_list = [list(input().split()) for _ in range(relation_count)]
