import sys

sys.stdin = open('input.txt', 'r')


def list2int(num_list):
    return int(''.join(list(map(str, num_list))))


def change(num_list, pointer, depth):
    global mx
    global count
    if depth == count:
        mx = max(mx, list2int(num_list))
        return

    N = len(num_list)
    sorted_num_list = sorted(num_list, reverse=True)
    for idx in range(pointer, N):
        if num_list[idx] != sorted_num_list[idx]:
            new_pointer = idx
            break
    else:
        if num_list.count(max(num_list)) == 1 and (depth - count) % 2:
            num_list[N - 1], num_list[N - 2] = num_list[N - 2], num_list[N - 1]
        mx = max(mx, list2int(num_list))
        return

    for idx in range(new_pointer + 1, N):
        if num_list[idx] == sorted_num_list[new_pointer]:
            new_num_list = num_list[:]
            new_num_list[new_pointer], new_num_list[idx] = new_num_list[idx], new_num_list[new_pointer]
            change(new_num_list, new_pointer, depth + 1)


T = int(input())

for tc in range(1, T + 1):
    money, count = input().split()
    money = list(map(int, list(money)))
    count = int(count)
    mx = 0
    change(money, 0, 0)

    print('#{} {}'.format(tc, mx))