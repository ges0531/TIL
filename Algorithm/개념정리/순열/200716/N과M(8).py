def perm(origin_list, new_list, visited, count, flag):
    if len(new_list) == count:
        print(' '.join(map(str, new_list)))
        return
    for i in range(flag, len(origin_list)):
        new_list.append(origin_list[i])
        perm(origin_list, new_list, visited, count, i)
        new_list.pop()


def solution(n, m):
    number_list = list(map(int, input().split()))
    number_list.sort()
    perm(number_list, [], [0]*len(number_list), m, 0)

n, m = map(int, input().split())
solution(n, m)
# solution(4, 2)
