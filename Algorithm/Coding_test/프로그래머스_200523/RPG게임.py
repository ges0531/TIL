def tree(tr_list, index):
    global num_list
    if tr_list[index]:
        for ii in tr_list[index]:
            return num_list[index]+ tree(tr_list, ii)
    else:
        num_list[index] = 1
        return num_list[index]

def solution(total_sp, skills):
    global num_list
    tree_list = [[] for _ in range(len(skills)+2)]
    num_list = [0]*(len(skills)+2)
    for k in range(len(skills)):
        tree_list[skills[k][0]].append(skills[k][1])
    print(tree_list)
    for i in range(len(tree_list)):
        print(tree(tree_list, i))
    print(num_list)
    return 1

solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]])