import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    strings = list(input())
    count = 0
    while count != len(strings)-1:
        if strings[count] == strings[count+1]:
            strings.pop(count)
            strings.pop(count)
            count = 0
        else:
            count += 1
    print('#{} {}'.format(test_case, len(strings)))