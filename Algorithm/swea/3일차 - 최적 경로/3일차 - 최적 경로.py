import sys
# import time
#time.time()-stime
#stime = time.time()

sys.stdin = open('input.txt', 'r')


def short_track(start_node):
    global result, visited
    queue = [start_node]
    print(queue, 1)
    visited[start_node[0]][start_node[1]] = 1
    end_node = []
    while queue:
        a = queue.pop(0)
        for k in range(4):
            y = a[0]
            x = a[1]
            idy = y + dy[k]
            idx = x + dx[k]
            if 0 <= idy < 101 and 0 <= idx < 101:
                if visited[idy][idx] == 0:
                    if matrix[idy][idx] == 0 or matrix[idy][idx] == 1:
                        visited[idy][idx] = visited[y][x] + 1
                        queue.append([idy, idx])
                        if matrix[idy][idx] == 1:
                            result += visited[idy][idx]-1
                            end_node.append([idy, idx])
                            print(end_node, 2)

        if len(end_node) >= 1:
            break
    print(end_node, 3)
    return end_node.pop()



T = int(input())

for test_case in range(1, T+1):
    customer_count = int(input())
    location = list(map(int, input().split()))
    customer_location = [0] * (len(location)//2)
    visited = [[0] * 101 for _ in range(101)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0
    for i in range(len(location)//2):
        customer_location[i] = [location[2*i], location[2*i+1]]
    work_location = customer_location.pop(0)
    home_location = customer_location.pop(0)
    matrix = [[0]*101 for _ in range(101)]

    for j in range(len(customer_location)):
        matrix[customer_location[j][0]][customer_location[j][1]] = 1

    change_location = work_location
    for track in range(customer_count):
        change_location = short_track(change_location)
    last_result = abs(change_location[0]-home_location[0])+abs(change_location[1]-home_location[1])
    ans = result + last_result
    print('#{} {}'.format(test_case, ans))
