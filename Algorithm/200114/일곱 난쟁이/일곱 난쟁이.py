import sys

sys.stdin = open('input.txt', 'r')
height_list = [int(input()) for _ in range(9)]
visited = [0]*len(height_list)


def solution(index, result_list):
    global flag
    if len(result_list) == 7 and sum(result_list) == 100:
        if flag:
            result = sorted(result_list)
            flag = 0
            for j in result:
                print(j)
        return
    for i in range(index, len(height_list)):
        if not visited[i]:
            result_list.append(height_list[i])
            visited[i] = 1
            solution(index+1, result_list)
            visited[i] = 0
            result_list.pop()

flag = 1
solution(0, [])