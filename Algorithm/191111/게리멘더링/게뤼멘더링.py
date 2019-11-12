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
    global visited, my_min
    if r == 0:
        result_1 = t[:]
        result_2 = []
        result = 0
        visited = [0]*area_count
        for a in range(len(arr)):
            if arr[a] not in t:
                result_2.append(arr[a])
        for link_1 in range(1, len(result_1)):
            result += BFS(result_1[0], result_1[link_1])
        if result == len(result_1)-1:
            for link_1 in range(len(result_1)):
                visited[result_1[link_1]] = 1
        result = 0
        for link_2 in range(1, len(result_2)):
            result += BFS(result_2[0], result_2[link_2])
        if result == len(result_2)-1:
            for link_2 in range(len(result_2)):
                visited[result_2[link_2]] = 1
        print(result_1, result_2)
        rere_1 = 0
        rere_2 = 0
        if visited.count(1) == area_count:
            print(result_1, result_2)
            for re_1 in range(len(result_1)):
                rere_1 += people_list[result_1[re_1]]
            for re_2 in range(len(result_2)):
                rere_2 += people_list[result_2[re_2]]
            if my_min > abs(rere_1-rere_2):
                my_min = abs(rere_1-rere_2)



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


