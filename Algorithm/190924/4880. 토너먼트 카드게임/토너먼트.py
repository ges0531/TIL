import sys

sys.stdin = open('input.txt', 'r')


def merge_sort(list):
    print(list)
    print(result, 111)
    global a, result
    if len(list) == 2:
        print(list)
        if list[0][0] == '1':
            if list[1][0] == '3':
                a = list[0]
                result.append(a)
            elif list[1][0] == '2':
                a = list[1]
                result.append(a)
            elif list[1][0] == '1':
                if int(list[0][1]) > int(list[1][1]):
                    a = list[1]
                else:
                    a = list[0]
                result.append(a)
        elif list[0][0] == '2':
            if list[1][0] == '3':
                a = list[1]
                result.append(a)
            elif list[1][0] == '1':
                a = list[0]
                result.append(a)
            elif list[1][0] == '2':
                if int(list[0][1]) > int(list[1][1]):
                    a = list[1]
                else:
                    a = list[0]
                result.append(a)
        elif list[0][0] == '3':
            if list[1][0] == '1':
                a = list[1]
                result.append(a)
            elif list[1][0] == '2':
                a = list[0]
                result.append(a)
            elif list[1][0] == '3':
                if int(list[0][1]) > int(list[1][1]):
                    a = list[1]
                else:
                    a = list[0]
                result.append(a)
    if len(list) == 1:
        a = list[0]
        return a
    mid = len(list) // 2
    if len(list)==3:
        leftList = list[:mid+1]
        rightList = list[mid+1:]
        merge_sort(leftList)
        merge_sort(rightList)
    else:
        leftList = list[:mid]
        rightList = list[mid:]
        merge_sort(leftList)
        merge_sort(rightList)
    return a


T = int(input())

for test_case in range(1, T+1):
    people_count = int(input())
    people_list = list(map(int, input().split()))
    people_list_2 = list(map(str, people_list))
    result = []
    for i in range(len(people_list_2)):
        people_list_2[i] += str(i+1)
    print('#{} {}'.format(test_case, merge_sort(people_list_2)))