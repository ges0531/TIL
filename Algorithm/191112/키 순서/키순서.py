import sys

sys.stdin = open('input.txt', 'r')

def BFS(start_node, link):
    global count
    queue = [start_node]
    visited = [0] * (student_count + 1)
    visited[start_node] = 1
    while queue:
        a = queue.pop(0)
        for k in range(len(link[a])):
            if not visited[link[a][k]]:
                visited[link[a][k]] = 1
                count += 1
                queue.append(link[a][k])


T = int(input())

for test_case in range(1, T+1):
    student_count = int(input())
    link_count = int(input())
    link_list = [list(map(int, input().split())) for _ in range(link_count)]
    big_link = [[] for _ in range(student_count+1)]
    small_link = [[] for _ in range(student_count+1)]
    result = 0
    for i in range(len(link_list)):
        big_link[link_list[i][0]].append(link_list[i][1])
        small_link[link_list[i][1]].append(link_list[i][0])
    for j in range(1, student_count+1):
        count = 0
        if big_link[j]:
            BFS(j, big_link)
        if small_link[j]:
            BFS(j, small_link)
        if count == student_count-1:
            result += 1
    print('#{} {}'.format(test_case, result))