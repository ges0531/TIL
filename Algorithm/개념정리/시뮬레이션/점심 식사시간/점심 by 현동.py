import sys

sys.stdin = open('input.txt')

def sol(people_idx, stair_idx):
    s_time = stairs[stair_idx][2]
    stair_state = [0] * len(people_idx)

    waiting_list = []
    for p in people_idx:
        waiting_list.append(time_info[stair_idx][p])
    waiting_list.sort()
    time = 0

    s_cnt, s_idx, s_front = 0, 0, 0
    front, end = 0, len(waiting_list)

    while True:
        for i in range(front, end):
            if waiting_list[i] < time:
                if s_cnt < 3:
                    stair_state[s_idx] = s_time
                    s_cnt += 1
                    s_idx += 1
                    front += 1
                else:
                    break

        for i in range(s_front, s_idx):
            stair_state[i] -= 1
            if stair_state[i] == 0:
                s_front += 1
                s_cnt -= 1

        if s_cnt < 0: s_cnt = 0
        time += 1

        if s_front == end: break

    return time

T = int(input())
T = 1
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    tmp_people = []
    stairs = []
    for x in range(n):
        for y in range(n):
            if arr[x][y]:
                if arr[x][y] == 1:
                    tmp_people.append((x, y))
                else:
                    stairs.append((x, y, arr[x][y]))

    people_len = len(tmp_people)
    time_info = [[0] * people_len for _ in range(2)]

    sx1, sy1, t1 = stairs[0]
    sx2, sy2, t2 = stairs[1]
    for idx, (px, py) in enumerate(tmp_people):
        time_info[0][idx] = abs(px - sx1) + abs(py - sy1)
        time_info[1][idx] = abs(px - sx2) + abs(py - sy2)

    idx = set(range(people_len))
    power_set = [[]]
    for i in idx:
        tmp = [[i] + p for p in power_set]
        power_set += tmp

    min_time = 9999999
    for i in range(2 ** people_len):
        tmp_time = max(sol(power_set[i], 0), sol(power_set[-1 - i], 1))
        min_time = min(tmp_time, min_time)

    print('#%d %d' % (tc, min_time))