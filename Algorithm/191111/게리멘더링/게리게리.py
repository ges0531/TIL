import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node, link):
    queue = [start_node]
    while queue:
        a = queue.pop(0)
        if not visited[a]:
            visited[a] = 1
            for ii in range(len(link_list[a])):
                if not visited[link_list[a][ii]]:
                    queue.append(link_list[a][ii])
    for li in range(len(link)):
        if not visited[link[li]]:
            return False
    return True




def comb(n, r, arr, t):
    global visited, my_min
    if r == 0:
        result_1 = t[:]
        result_2 = []
        for a in range(len(arr)):
            if arr[a] not in t:
                result_2.append(arr[a])
        visited = [0] * area_count
        flag = 0
        if BFS(result_1[0], result_1):
            if BFS(result_2[0], result_2):
                flag = 1
        if flag:
            ans_1 = 0
            ans_2 = 0
            for s in range(len(result_1)):
                ans_1 += people_list[result_1[s]]
            for ss in range(len(result_2)):
                ans_2 += people_list[result_2[ss]]
            if my_min > abs(ans_1-ans_2):
                my_min = abs(ans_1-ans_2)

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
my_min = 100000000
for i in range(area_count):
    for j in range(len(link_list[i])):
        link_list[i][j] -= 1
    link_list[i].pop(0)
for co in range(1, area_count):
    comb(area_count, co, index_list, [0]*co)

if my_min == 100000000:
    print(-1)
else:
    print(my_min)


