import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    bus_line_count = int(input())
    bus_line_list = [list(map(int, input().split())) for _ in range(bus_line_count)]
    bus_stop_count = int(input())
    bus_stop = [int(input()) for _ in range(bus_stop_count)]
    result = [0] * bus_stop_count
    for i in range(len(bus_stop)):
        count = 0
        for j in range(len(bus_line_list)):
            if bus_stop[i] >= bus_line_list[j][0] and bus_stop[i] <= bus_line_list[j][1]:
                count += 1
        result[i] = count
    print('#{} {}'.format(test_case, ' '.join(map(str, result))))