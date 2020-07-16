def perm(origin_list, new_list, visited, count, flag, perm_visited):
    if len(new_list) == count:
        perm_visited[''.join(map(str, new_list))] = 1
        print(' '.join(map(str, new_list)))
        return
    for i in range(flag, len(origin_list)):
        new_list.append(origin_list[i])
        if ''.join(map(str, new_list)) not in perm_visited:
            perm(origin_list, new_list, visited, count, i, perm_visited)
        new_list.pop()


def solution(n, m):
    number_list = list(map(int, input().split()))
    number_list.sort()
    perm(number_list, [], [0]*len(number_list), m, 0, {})

n, m = map(int, input().split())
solution(n, m)
# solution(4, 2)
