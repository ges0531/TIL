def solution(s):
    s = list(s)
    count = 1
    real_result = []
    while count <= len(s)-1:
        if s[count] == '{':
            a = ''
            my_list = []
            while s[count] != '}':
                if s[count] == ',':
                    my_list.append(int(a))
                    a = ''
                elif s[count] != '{':
                    a += s[count]
                count += 1
            my_list.append(int(a))
            real_result.append(my_list)
        else:
            count += 1
    result_list = [0]*len(real_result)
    for i in range(len(real_result)):
        result_list[len(real_result[i])-1] = real_result[i]
    result_list = sum(result_list, [])
    answer = []
    for j in range(len(result_list)):
        if not result_list[j] in answer:
            answer.append(result_list[j])

    return answer


s = "{{20,111},{111}}"
print(solution(s))
