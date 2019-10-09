import sys

sys.stdin = open('input.txt', 'r')

string_length = int(input())

string = list(input())
operator_list = []
num_list = []
for i in range(string_length):
    if i % 2:
        operator_list.append(string[i])
    else:
        num_list.append(string[i])
num_list = list(map(int, num_list))

