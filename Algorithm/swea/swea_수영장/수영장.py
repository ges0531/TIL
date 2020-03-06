import sys

sys.stdin = open('input.txt', 'r')


def min_cash(date, index, result):
    global my_min
    if result > my_min:
        return
    if index == 12:
        my_min = min(my_min, result)
        return
    if date_list[index] == 0:
        min_cash(date, index+1, result)
    else:
        if date == 0:
            date_list[index] -= 1
            min_cash(0, index, result+cash_list[0])
            min_cash(1, index, result + cash_list[1])
            min_cash(2, index, result + cash_list[2])
            min_cash(3, index, result + cash_list[3])
            date_list[index] += 1
        elif date == 1:
            temp = date_list[index]
            date_list[index] = 0
            min_cash(0, index+1, result + cash_list[0])
            min_cash(1, index+1, result + cash_list[1])
            min_cash(2, index+1, result + cash_list[2])
            min_cash(3, index+1, result + cash_list[3])
            date_list[index] = temp
        elif date == 2:
            temp_1 = date_list[index]
            temp_2 = 0
            temp_3 = 0
            date_list[index] = 0
            if index+1 < 12:
                temp_2 = date_list[index+1]
                date_list[index + 1] = 0
            if index+2 < 12:
                temp_3 = date_list[index+2]
                date_list[index + 2] = 0
            if index+3 <= 12:
                min_cash(0, index+3, result + cash_list[0])
                min_cash(1, index+3, result + cash_list[1])
                min_cash(2, index+3, result + cash_list[2])
                min_cash(3, index+3, result + cash_list[3])
            else:
                min_cash(0, 12, result + cash_list[0])
                min_cash(1, 12, result + cash_list[1])
                min_cash(2, 12, result + cash_list[2])
                min_cash(3, 12, result + cash_list[3])
            date_list[index] = temp_1
            if index + 1 < 12:
                date_list[index + 1] = temp_2
            if index + 2 < 12:
                date_list[index + 2] = temp_3
        else:
            temp_list = date_list[:]
            for i in range(len(date_list)):
                date_list[i] = 0
            min_cash(3, 12, result + cash_list[3])
            for j in range(len(date_list)):
                date_list[j] = temp_list[j]





T = int(input())
for test_case in range(1, T+1):
    cash_list = list(map(int, input().split()))
    date_list = list(map(int, input().split()))
    visited = [100000000]*12
    my_min = 100000000
    for i in range(4):
        min_cash(0, 0, 0)
    print(my_min)
