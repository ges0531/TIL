def perm(origin_list, new_list, visited, count, perm_visited):
    if len(new_list) == count and ''.join(map(str, new_list)) not in perm_visited:
        perm_visited[''.join(map(str, new_list))] = 1
        print(' '.join(map(str, new_list)))
        return
    for i in range(len(origin_list)):
        if not visited[i]:
            visited[i] = 1
            new_list.append(origin_list[i])
            perm(origin_list, new_list, visited, count, perm_visited)
            new_list.pop()
            visited[i] = 0

def solution(n, m):
    number_list = [9, 7, 9, 1]
    number_list = list(map(int, input().split()))
    number_list.sort()
    perm(number_list, [], [0]*len(number_list), m, {})


n, m = map(int, input().split())
# n, m = 4, 2
solution(n, m)
