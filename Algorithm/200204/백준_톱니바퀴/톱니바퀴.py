import sys

sys.stdin = open('input.txt', 'r')


def right_spin(current_list):
    flag_front = current_list.pop()
    current_list = [flag_front] + current_list
    return current_list


def left_spin(current_list):
    flag_back = current_list.pop(0)
    current_list = current_list + [flag_back]
    return current_list


def add_spin(spin_index, flag_index):
    if flag_index >= 4 or flag_index < 0:
        return
    if spin_index == 1:
        gear_list[flag_index] = right_spin(gear_list[flag_index])
        visited[flag_index] = 1
        if (flag_index+1 != 4) and (gear_list[flag_index][2] != gear_list[flag_index+1][6]):
            add_spin(-1, flag_index+1)
        if (flag_index-1 != -1) and (gear_list[flag_index][6] != gear_list[flag_index-1][2]):
            add_spin(-1, flag_index-1)
    else:
        gear_list[flag_index] = left_spin(gear_list[flag_index])
        if (flag_index+1 != 4) and (gear_list[flag_index][2] != gear_list[flag_index+1][6]):
            add_spin(1, flag_index+1)
        if (flag_index-1 != -1) and (gear_list[flag_index][6] != gear_list[flag_index-1][2]):
            add_spin(1, flag_index-1)


gear_list = [list(map(int, input())) for _ in range(4)]
spin_count = int(input())
spin_list = [list(map(int, input().split())) for _ in range(spin_count)]
result = 0
result_flag = 1

for i in range(spin_count):
    visited = [0] * 4
    add_spin(spin_list[i][1], spin_list[i][0]-1)
for j in range(4):
    if gear_list[j][0] == 1:
        result += result_flag
    result_flag *= 2
print(result)