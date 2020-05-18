def solution(expression):
    global ans
    ans = 0
    num = ''
    result = []
    for j in expression:
        if j in ['+', '-', '*']:
            result.append(int(num))
            result.append(j)
            num = ''
        else:
            num += j
    else:
        result.append(int(num))
    perm(['+', '-', '*'], [], [0]*3, result)
    return ans


def perm(origin_list, new_list, visited, cal_list):
    global ans
    if len(new_list) == 3:
        copy_cal_list = cal_list[:]
        for kk in range(3):
            for k in range(len(copy_cal_list)-1):
                if copy_cal_list[k] == new_list[kk]:
                    copy_cal_list[k+1] = calcu(copy_cal_list[k], copy_cal_list[k-1], copy_cal_list[k+1])
                    copy_cal_list[k] = 0
                    copy_cal_list[k-1] = 0
            print(copy_cal_list)
            my_list = []
            for z in range(len(copy_cal_list)):
                if copy_cal_list[z] != 0:
                    my_list.append(copy_cal_list[z])
            copy_cal_list = my_list[:]
        ans = max(ans, abs(copy_cal_list[0]))
        return
    for i in range(len(origin_list)):
        if not visited[i]:
            visited[i] = 1
            new_list.append(origin_list[i])
            perm(origin_list, new_list, visited, cal_list)
            new_list.pop()
            visited[i] = 0


def calcu(operator, x, y):
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y
    else:
        return x*y

solution("50*6-3*2")