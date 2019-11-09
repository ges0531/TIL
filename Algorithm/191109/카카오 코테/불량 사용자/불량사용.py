def solution(user_id, banned_id):
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
    lulu = []
    for _ in range(len(answer)):
        result = []
        visited = []
        for ans_1 in range(len(answer)):
            for ans_2 in range(len(answer)):
                if answer[ans_1][ans_2] not in visited:
                    result.append(answer[ans_1][ans_2])
                    visited.append(answer[ans_1][ans_2])
                    break
        lulu.append(result)
    print(lulu)
    return answer


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))