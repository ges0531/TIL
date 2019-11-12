import sys

sys.stdin = open('input.txt', 'r')

def DFS(start_node, link):
    global visited, result_visited
    for k in range(len(link[start_node])):
        if not visited[link[start_node][k]]:
            visited[link[start_node][k]] = 1
            result_visited[link[start_node][k]] = 1
            DFS(link[start_node][k], link)
            visited[link[start_node][k]] = 0


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
        result_visited = [0] * (student_count + 1)
        visited = [0]*(student_count+1)
        if big_link[j]:
            DFS(j, big_link)
        visited = [0] * (student_count + 1)
        if small_link[j]:
            DFS(j, small_link)
        if sum(result_visited) == 5:
            result += 1
    print('#{} {}'.format(test_case, result))
