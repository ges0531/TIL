def solution(answer_sheet, sheets):
    answer = []
    answer_2 = []
    for i in range(len(sheets)):
        for j in range(i+1, len(sheets)):
            result = []
            for k in range(len(sheets[i])):
                if sheets[i][k] == sheets[j][k]:
                    result.append(sheets[i][k])
                else:
                    result.append(0)
            answer.append(result)
    for ii in range(len(answer)):
        result_2 = []
        for jj in range(len(answer_sheet)):
            if answer[ii][jj] and answer_sheet[jj] != answer[ii][jj]:
                result_2.append(answer[ii][jj])
            else:
                result_2.append(0)
        answer_2.append(result_2)
    ans = []
    for kk in answer_2:
        flag = 0
        flag_2 = 0
        my_max = 0
        for kkk in kk:
            if kkk:
                flag += 1
                flag_2 += 1
            else:
                my_max = max(flag_2, my_max)
                flag_2 = 0
        my_max = max(flag_2, my_max)
        ans.append([flag, my_max**2])
    print(ans)
    real_answer = max((map(sum, ans)))

    return real_answer


solution("24551", ["24553", "24553", "24553", "24553"])