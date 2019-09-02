import sys

sys.stdin = open('input.txt', 'r')

def divide(m):
    if len(m) <= 1:
        return m
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]
    left = divide(left)
    right = divide(right)
    print(left, right)
    # if len(left) == 1 and len(right) == 1:
    #     if left[0] == 1:
    #         if right[0] == 2:
    #             print(right)
    #         else:
    #             print(left)
    #     elif left[0] == 2:
    #         if right[0] == 3:
    #             print(right)
    #         else:
    #             print(left)
    #     elif left[0] == 3:
    #         if right[0] == 1:
    #             print(right)
    #         else:
    #             print(left)
T = int(input())

for test_case in range(1, T+1):
    print(test_case, '--')
    people_count = int(input())
    new_game = list(map(int, input().split()))
    divide(new_game)
