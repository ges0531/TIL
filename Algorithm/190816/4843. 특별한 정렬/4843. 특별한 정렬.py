import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    integer_count = int(input())
    unordered_num = list(map(int, input().split()))
    unordered_num.sort()
    my_box = []
    for i in range(5):
        my_box.append(str(unordered_num[-i - 1]))
        my_box.append(str(unordered_num[i]))
    my_box = ' '.join(my_box)
    print('#{} {}'.format(test_case, my_box))