import sys

sys.stdin = open('input.txt', 'r')


def merge_sort(list):
    if len(list) <= 2:
        if len(list) == 1:
            return list[0]
        else:
            if list[0] == 1:
                if list[1] == 3:
                    return 1
                elif list[1] == 2:
                    return 2
            elif list[0] == 2:
                if list[1] == 3:
                    return 3
                elif list[1] == 1:
                    return 2
            elif list[0] == 3:
                if list[1] == 1:
                    return 1
                elif list[1] == 2:
                    return 3
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    merge_sort(leftList)
    merge_sort(rightList)
    print(leftList, rightList)


T = int(input())

for test_case in range(1, T+1):
    people_count = int(input())
    people_list = list(map(int, input().split()))
    print(merge_sort(people_list))
    print()