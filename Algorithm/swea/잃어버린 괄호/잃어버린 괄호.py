import sys

sys.stdin = open('input.txt', 'r')


result_list = list(input().split('-'))
result_num = 0
for i in range(len(result_list)):
    if '+' in result_list[i]:
        result_list[i] = sum(map(int, result_list[i].split('+')))
result_list = list(map(int, result_list))
for j in range(1, len(result_list)):
    result_num -= result_list[j]

print(result_list[0]+result_num)