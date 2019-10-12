import sys

sys.stdin = open('input.txt', 'r')

string_length = int(input())

string = list(input())
copy_string = string[:]
my_real_list = []
my_real_list_2 = []
operator_list = []
operator_list_2 = []
while len(copy_string) >= 3:
    my_list = [0] * 3
    for i in range(3):
        my_list[i] = copy_string.pop(0)
    if copy_string:
        operator_list.append(copy_string.pop(0))
    my_real_list.append(my_list)

while len(string) >= 5:
    my_list = [0] * 3
    for i in range(3):
        my_list[i] = string.pop(2)
    if string:
        operator_list_2.append(string.pop(1))
    my_real_list_2.append(my_list)