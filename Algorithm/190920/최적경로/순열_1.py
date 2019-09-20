import sys

sys.stdin = open('input.txt', 'r')

def perm(arr, path, k, visited, start_node, end_node, result):
    global my_min
    if len(arr) == len(path):
        if path[0] == start_node:
            if path[-1] == end_node:
                if result < my_min:
                    my_min = result

    else:
        for i in range(1, len(arr)):
            if visited[i]:
                continue
            visited[i] = 1
            path.append(arr[i])
            result += abs(path[-1][0]-path[-2][0]) + abs(path[-1][1] - path[-2][1])
            if result < my_min:
                perm(arr, path, k+1, visited, start_node, end_node, result)
            result -= (abs(path[-1][0] - path[-2][0]) + abs(path[-1][1] - path[-2][1]))
            visited[i] = 0
            path.pop()


T = int(input())
for test_case in range(1, T+1):
    customer_count = int(input())
    location = list(map(int, input().split()))
    customer_location = [location[i:i+2] for i in range(0, len(location), 2)]
    home_location = customer_location[1]
    work_location = customer_location[0]
    my_min = 1000000000000000
    perm(customer_location, [customer_location[0]], 0, [0]*len(customer_location), work_location, home_location, 0)
    print('#{} {}'.format(test_case, my_min))