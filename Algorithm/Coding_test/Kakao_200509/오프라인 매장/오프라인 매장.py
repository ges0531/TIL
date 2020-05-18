def solution(gems):
    set_list = []
    for new_1 in gems:
        if new_1 not in set_list:
            set_list.append(new_1)
    set_list.sort()
    for i in range(len(set_list)-1, len(gems)):
        for j in range(len(gems)-i):
            new_list = []
            for k in gems[j:j+i+1]:
                if k not in new_list:
                    new_list.append(k)
            new_list.sort()
            if set_list == new_list:
                return [j+1, j+i+1]


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])