import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node, end_node):
    queue = [start_node]
    visited_1 = [0]*area_count
    while queue:
        a = queue.pop(0)
        if not visited_1[a]:
            visited_1[a] = 1
            for ii in range(len(link_list[a])):
                if not visited_1[link_list[a][ii]]:
                    visited_1[link_list[a][ii]] = 1
                    queue.append(link_list[a][ii])
    if visited_1[start_node] and visited_1[end_node]:
        return 1
    else:
        return 0




def comb(n, r, arr, t):
    if r == 0:
        result_1 = t[:]
        result_2 = []

    elif r > n:
        return
    else:
        t[r-1] = arr[n-1]
        comb(n-1, r-1, arr, t)
        comb(n-1, r, arr, t)


area_count = int(input())
people_list = list(map(int, input().split()))
link_list = [list(map(int, input().split())) for _ in range(area_count)]
index_list = [j for j in range(area_count)]
visited = [0] * area_count
my_min = 100000000
for i in range(area_count):
    for j in range(len(link_list[i])):
        link_list[i][j] -= 1
    link_list[i].pop(0)
for co in range(1, area_count):
    comb(area_count, co, index_list, [0]*co)

print(my_min)


