def perm(origin_list, new_list, visited):
    if len(new_list) == len(origin_list):
        print(new_list)
        return
    for i in range(len(origin_list)):
        if not visited[i]:
            visited[i] = 1
            new_list.append(origin_list[i])
            perm(origin_list, new_list, visited)
            new_list.pop()
            visited[i] = 0

def comb(origin_list, new_list, select, visited, k):
    if len(new_list) == select:
        print(new_list)
        return
    elif select > len(origin_list):
        return
    for i in range(k, len(origin_list)):
        if not visited[i]:
            visited[i] = 1
            new_list.append(origin_list[i])
            comb(origin_list, new_list, select, visited, k+1)
            new_list.pop()
            visited[i] = 0

comb([1, 2, 3, 4], [], 2, [0]*4, 0)
