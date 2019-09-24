import sys

sys.stdin = open('input.txt', 'r')


def merge_sort(list):
    global a, b
    if len(list) <= 2:
        if len(list) == 1:
            a = list[0]
            b = people_list.index(list[0])
            return a
        else:
            if list[0] == list[1]:
                if people_list.index(list[0]) > people_list.index(list[1]):
                    a = list[1]
                    b = people_list.index(list[1])
                    return a
                else:
                    a = list[0]
                    b = people_list.index(list[0])
                    return a
            if list[0] == 1:
                if list[1] == 3:
                    a = 1
                    b = people_list.index(list[0])
                    return a
                elif list[1] == 2:
                    a = 2
                    b = people_list.index(list[1])
                    return a
            elif list[0] == 2:
                if list[1] == 3:
                    a = 3
                    b = people_list.index(list[1])
                    return a
                elif list[1] == 1:
                    a = 2
                    b = people_list.index(list[0])
                    return a
            elif list[0] == 3:
                if list[1] == 1:
                    a = 1
                    b = people_list.index(list[1])
                    return a
                elif list[1] == 2:
                    a = 3
                    b = people_list.index(list[0])
                    return a
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    merge_sort(leftList)
    merge_sort(rightList)
    return b+1


T = int(input())

for test_case in range(1, T+1):
    people_count = int(input())
    people_list = list(map(int, input().split()))
    print('#{} {}'.format(test_case, merge_sort(people_list)))