import sys

sys.stdin = open('input.txt','r')

def search_num(num, index_flag, operator):
    global my_max, my_min
    if index_flag == number_count:
        if num > my_max:
            my_max = num
        if num < my_min:
            my_min = num
        return
    for i in range(4):
        if i == 0 and operator_list[i]:
            operator[0] -= 1
            search_num(num+number_list[index_flag], index_flag+1, operator)
            operator[0] += 1
        elif i == 1 and operator_list[i]:
            operator[1] -= 1
            search_num(num - number_list[index_flag], index_flag + 1, operator)
            operator[1] += 1
        elif i == 2 and operator_list[i]:
            operator[2] -= 1
            search_num(num * number_list[index_flag], index_flag + 1, operator)
            operator[2] += 1
        elif i == 3 and operator_list[i]:
            operator[3] -= 1
            search_num((int(num / number_list[index_flag])), index_flag + 1, operator)
            operator[3] += 1


number_count = int(input())
number_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
my_max = -10000000000
my_min = 10000000000
search_num(number_list[0], 1, operator_list)
print(my_max)
print(my_min)