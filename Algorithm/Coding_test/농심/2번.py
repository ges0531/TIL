my_max = 0


def perm(good_list, box_list, visited, flag, new_list):
    global my_max
    if flag == len(good_list):
        if len(new_list[:]) > my_max:
            my_max = len(new_list[:])
        return
    for i in range(len(box_list)):
        if not visited[i]:
            if good_list[flag] <= box_list[i]:
                visited[i] = 1
                new_list.append(good_list[flag])
                perm(good_list, box_list, visited, flag + 1, new_list)
                new_list.pop()
                visited[i] = 0
            else:
                perm(good_list, box_list, visited, flag + 1, new_list)


def solution(goods, boxes):
    global my_max
    answer = 0
    perm(goods, boxes, [0] * len(boxes), 0, [])
    return my_max