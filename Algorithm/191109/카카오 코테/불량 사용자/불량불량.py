def solution(user_id, banned_id):
    from itertools import product
    answer = []
    for i in range(len(banned_id)):
        my_list = []
        for j in range(len(user_id)):
            count = 0
            for k in range(len(banned_id[i])):
                if len(banned_id[i]) == len(user_id[j]):
                    if banned_id[i][k] == user_id[j][k] or banned_id[i][k] == '*':
                        count += 1
            if count == len(user_id[j]):
                my_list.append(user_id[j])
        answer.append(my_list)
    answer = list(map(set, product(*answer)))
    print(answer)
    result = []
    for ans in range(len(answer)):
        if len(answer[ans]) == len(banned_id) and answer[ans] not in result:
            result.append(answer[ans])
    return len(result)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))