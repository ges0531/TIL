import sys

sys.stdin = open('input.txt', 'r')


def spin_right(current_list, k):
    for _ in range(k):
        flag_front = current_list.pop()
        current_list = [flag_front]+current_list
    return current_list


def spin_left(current_list, k):
    for _ in range(k):
        flag_back = current_list.pop(0)
        current_list = current_list + [flag_back]
    return current_list


def BFS(start_node):
    global adjacency_flag
    queue = [start_node]
    visited = [[0]*circle_length for _ in range(circle_count)]
    visited[start_node[0]][start_node[1]] = 1
    check_list = []
    while queue:
        a = queue.pop(0)
        for ii in range(4):
            y = a[0]
            x = a[1]
            idy = y+dy[ii]
            idx = x+dx[ii]
            if 0 <= idy < circle_count and 0 <= idx < circle_length:
                if circle_list[y][x] and (circle_list[y][x] == circle_list[idy][idx]):
                    check_list.append([y, x])
                    check_list.append([idy, idx])
                    adjacency_flag = 0
                if not visited[idy][idx]:
                    visited[idy][idx] = 1
                    queue.append([idy, idx])
    for jj in range(circle_count):
        if circle_list[jj][0] == circle_list[jj][-1]:
            check_list.append([jj, 0])
            check_list.append([jj, -1])
    print(check_list)
    return check_list


circle_count, circle_length, spin_count = map(int, input().split())
circle_list = [list(map(int, input().split())) for _ in range(circle_count)]
spin_list = [list(map(int, input().split())) for _ in range(spin_count)]
my_sum = sum(sum(circle_list, []))
num_count = circle_count*circle_length
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for i in range(spin_count):
    memo = [[0] * circle_length for _ in range(circle_count)]
    flag_multiple = spin_list[i][0]
    adjacency_flag = 1
    while flag_multiple <= circle_count:
        if spin_list[i][1]:
            circle_list[flag_multiple - 1] = spin_left(circle_list[flag_multiple-1], spin_list[i][2])
        else:
            circle_list[flag_multiple - 1] = spin_right(circle_list[flag_multiple-1], spin_list[i][2])
        flag_multiple *= 2
    for check_y, check_x in BFS([0, 0]):
        if circle_list[check_y][check_x]:
            my_sum -= circle_list[check_y][check_x]
            circle_list[check_y][check_x] = 0
            num_count -= 1
    if adjacency_flag:
        for column in range(circle_count):
            for row in range(circle_length):
                if circle_list[column][row]:
                    if (my_sum / num_count) < circle_list[column][row]:
                        circle_list[column][row] -= 1
                    elif (my_sum / num_count) > circle_list[column][row]:
                        circle_list[column][row] += 1
print(my_sum)