def perm(origin_list, new_list, visited, count):
    if len(new_list) == count:
        print(' '.join(map(str, new_list)))
        return
    for i in range(len(origin_list)):
        if not visited[i]:
            visited[i] = 1
            new_list.append(origin_list[i])
            perm(origin_list, new_list, visited, count)
            new_list.pop()
            visited[i] = 0

def solution(n, m, number_list):
    perm(number_list, [], [0]*len(number_list), m)


n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
solution(n, m, n_list)
