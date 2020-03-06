import sys

sys.stdin = open('input.txt', 'r')


def perm(arr, path, visited, result, k):
    global my_min
    if k == len(arr):
        if result < my_min:
            my_min = result
    else:
        for i in range(len(arr)):
            if visited[i]:
                continue
            path.append(arr[i])
            visited[i] = 1
            if result + matrix[k][path[-1]] < my_min:
                perm(arr, path, visited, result + matrix[k][path[-1]], k+1)
            visited[i] = 0
            path.pop()

T = int(input())

for test_case in range(1, T+1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    perm_list = [i for i in range(size)]

    my_min = 100000000
    perm(perm_list, [], [0]*len(perm_list), 0, 0)
    print('#{} {}'.format(test_case, my_min))