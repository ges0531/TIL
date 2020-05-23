import itertools
def solution(n):
    three_list = []
    sum_list = []
    k = 0
    while len(sum_list) < n:
        if 3**k not in three_list:
            three_list.append(3**k)
        else:
            for i in range(len(three_list)):
                for j in itertools.combinations(three_list, i):
                    if sum(j) not in sum_list:
                        sum_list.append(sum(j))
            k += 1
    sum_list.sort()
    return sum_list[n]



print(solution(11))