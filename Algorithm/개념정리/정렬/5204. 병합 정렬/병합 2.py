import sys

sys.stdin = open('input.txt', 'r')


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    print(leftList, rightList)
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


def merge(left, right):
    global count
    result = []
    i = 0
    j = 0
    if left[-1] > right[-1]:
        count += 1
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while len(left) > i:
        result.append(left[i])
        i += 1
    while len(right) > j:
        result.append(right[j])
        j += 1
    return result


T = int(input())

for test_case in range(1, T+1):
    num_count = int(input())
    my_list = list(map(int, input().split()))
    count = 0
    print('#{} {} {}'.format(test_case, merge_sort(my_list)[num_count//2], count))
