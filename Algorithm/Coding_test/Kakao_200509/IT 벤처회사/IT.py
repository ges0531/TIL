def solution(expression):
    global ans
    num = ''
    result = []
    for j in expression:
        if j in ['+', '-', '*']:
            result.append(num)
            result.append(j)
            num = ''
        else:
            num += j
    else:
        result.append(num)
    print(result)
    ans = 0
    cal(1, int(result[0]), result)
    return ans


def cal(i, res, string):
    global ans
    N = len(string)
    if i == N:
        ans = max(abs(res), ans)
        return
    if string[i] == '+':
        cal(i+2, res+int(string[i+1]), string)
        if i == N-2:
            return
        x = int(string[i+1])
        operator = string[i+2]
        y = int(string[i+3])
        if operator == '+':
            cal(i+4, res+(x+y), string)
        elif operator == '-':
            cal(i+4, res + (x-y), string)
        else:
            cal(i+4, res+(x*y), string)
    elif string[i] == '-':
        cal(i + 2, res - int(string[i + 1]), string)
        if i == N - 2:
            return
        x = int(string[i + 1])
        operator = string[i + 2]
        y = int(string[i + 3])
        if operator == '+':
            cal(i + 4, res - (x + y), string)
        elif operator == '-':
            cal(i + 4, res - (x - y), string)
        else:
            cal(i + 4, res - (x * y), string)
    else:
        cal(i + 2, res * int(string[i + 1]), string)
        if i == N - 2:
            return
        x = int(string[i + 1])
        operator = string[i + 2]
        y = int(string[i + 3])
        if operator == '+':
            cal(i + 4, res * (x + y), string)
        elif operator == '-':
            cal(i + 4, res * (x - y), string)
        else:
            cal(i + 4, res * (x * y), string)

print(solution("50*6-3*2"))