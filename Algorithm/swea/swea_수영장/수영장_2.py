import sys

sys.stdin = open('input.txt', 'r')

def low_cash(cash, index, result):
    global my_min
    if result > my_min:
        return
    if index > 11:
        my_min = min(my_min, result)
        return
    if cash == 0:
        for i in range(4):
            low_cash(i, index+1, result+(cash_list[0]*date_list[index]))
    elif cash == 1:
        for i in range(4):
            low_cash(i, index+1, result+cash_list[1])
    elif cash == 2:
        for i in range(4):
            low_cash(i, index+3, result+cash_list[2])
    elif cash == 3:
        for i in range(4):
            low_cash(i, 12, result+cash_list[3])


T = int(input())
for test_case in range(1, T+1):
    cash_list = list(map(int, input().split()))
    date_list = list(map(int, input().split()))
    my_min = 1000000
    for i in range(4):
        low_cash(i, 0,  0)
    print('#{} {}'.format(test_case, my_min))