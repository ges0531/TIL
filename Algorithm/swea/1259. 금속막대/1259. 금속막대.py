import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    stick_count = int(input())
    thickness = list(map(int, input().split()))
    set_nasa = []
    result = []
    real_result = []
    for i in range(stick_count):
        nasa = [0] * 2
        nasa[0] = thickness[2*i]
        nasa[1] = thickness[2*i+1]
        set_nasa.append(nasa)
    for first in range(len(thickness)):
        if thickness.count(first) == 1:
            first_num = first

            for order in range(len(set_nasa)):
                if set_nasa[order][0] == first_num:
                    result.append(set_nasa[order])
                    for link in range(stick_count):
                        for link_2 in range(len(set_nasa)):
                            if result[link][1] == set_nasa[link_2][0]:
                                result.append(set_nasa[link_2])
    for j in range(len(result)):
        for k in range(len(result[j])):
            real_result.append(str(result[j][k]))
    print('#{} {}'.format(test_case, ' '.join(real_result)))
