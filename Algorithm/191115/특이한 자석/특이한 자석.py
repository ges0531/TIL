import sys

sys.stdin = open('input.txt', 'r')


def rotate_queue(k, r_list):
    if k == 1:
        a = r_list.pop()
        r_list = [a]+r_list
    else:
        a = r_list.pop(0)
        r_list = r_list+[a]
    return r_list

T = int(input())
T = 2
for test_case in range(1, T+1):
    rotation_count = int(input())
    magnetic_list = [list(map(int, input().split())) for _ in range(4)]
    rotation_list = [list(map(int, input().split())) for _ in range(rotation_count)]
    for ii in range(len(rotation_list)):
        rotation_list[ii][0] -= 1
    copy = [0]*8
    for i in range(rotation_count):
        for co_1 in range(8):
            copy[co_1] = magnetic_list[rotation_list[i][0]][co_1]
        if rotation_list[i][0]+1 < 4:
            if copy[2] != magnetic_list[rotation_list[i][0]+1][6]:
                magnetic_list[rotation_list[i][0]+1] = rotate_queue(-rotation_list[i][1], magnetic_list[rotation_list[i][0]+1])
        if rotation_list[i][0]-1 >= 0:
            if copy[6] != magnetic_list[rotation_list[i][0]-1][2]:
                magnetic_list[rotation_list[i][0]-1] = rotate_queue(-rotation_list[i][1], magnetic_list[rotation_list[i][0]-1])
        magnetic_list[rotation_list[i][0]] = rotate_queue(rotation_list[i][1], magnetic_list[rotation_list[i][0]])
        print(magnetic_list)
    result = magnetic_list[0][0] + 2*magnetic_list[1][0] + 4*magnetic_list[2][0] + 8*magnetic_list[3][0]
    print('#{} {}'.format(test_case, result))
    # [2, 6], [2, 6], [2, 6], [2, 6]