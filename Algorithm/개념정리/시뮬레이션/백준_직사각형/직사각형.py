import sys

sys.stdin = open('input.txt')

location_list = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    flag = 0
    flag_2 = 0
    flag_3 = 0
    flag_4 = 0
    if location_list[i][1] < location_list[i][5]:
        if location_list[i][3] < location_list[i][5]:
            flag += 1
        elif location_list[i][3] == location_list[i][5]:
            flag_3 += 1
    else:
        if location_list[i][1] > location_list[i][7]:
            flag += 1
        elif location_list[i][1] == location_list[i][7]:
            flag_3 += 1
    if location_list[i][0] < location_list[i][4]:
        if location_list[i][2] < location_list[i][4]:
            flag_2 += 1
        elif location_list[i][2] == location_list[i][4]:
            flag_4 += 1
    else:
        if location_list[i][0] > location_list[i][6]:
            flag_2 += 1
        elif location_list[i][0] == location_list[i][6]:
            flag_4 += 1
    if (flag == flag_2 == flag_3 == flag_4 == 0):
        print('a')
    elif (flag == flag_2 == 0 and flag_3 == flag_4 == 1):
        print('c')
    elif (flag == flag_2 == 1 and flag_3 == flag_4 == 0):
        print('d')
    else:
        print('b')

