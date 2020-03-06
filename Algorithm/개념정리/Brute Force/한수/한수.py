import sys

sys.stdin = open('input.txt', 'r')


def solution(number, count):
    if number < 1:
        print(count)
        return
    if number < 100:
        print(count+number)
        return
    num_list = list(map(int, list(str(number))))
    result = num_list[0] - num_list[1]
    for i in range(len(num_list)-1):
        if (num_list[i] - num_list[i+1]) != result:
            break
    else:
        count += 1
    solution(number-1, count)

solution(int(input()), 0)