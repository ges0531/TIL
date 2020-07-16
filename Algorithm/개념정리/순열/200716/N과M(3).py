def perm(origin_list, new_list, visited, count):
    if len(new_list) == count:
        print(' '.join(map(str, new_list)))
        return
    for i in range(len(origin_list)):
        new_list.append(origin_list[i])
        perm(origin_list, new_list, visited, count)
        new_list.pop()
def solution(n, m):
    number_list = [i+1 for i in range(n)]
    perm(number_list, [], [0]*len(number_list), m)

n, m = map(int, input().split())
solution(n, m)
# solution(4, 2)