import sys

sys.stdin = open('input.txt', 'r')

train_list = [list(map(int, input().split(' '))) for _ in range(4)]
result = 0
my_max = 0
for i in train_list:
    result -= i[0]
    result += i[1]
    if my_max < result:
        my_max = result
print(my_max)