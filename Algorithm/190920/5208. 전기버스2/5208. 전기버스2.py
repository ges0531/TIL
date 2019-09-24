import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    battery = list(map(int, input().split())) + [0]
    bus_stop_count = battery.pop(0)
    index = 0
    location = 0
    while location > len(battery):
        location += battery[index]
