priority = {'+': 0, '-': 0, '*': 1, '/': 1}
operater = ['+', '-', '*', '/', '(']
cal = '(6+5*(2-8)/2)'
stack = [0]*len(cal)
top = 0
my_list = [0]*len(cal)
k = 0
cal_2 = [0]*len(cal)
for i in range(len(cal)):
    if cal[i] in operater:
        if cal[i] == '(':
           stack[top] = cal[i]
           top += 1
        else:
            if priority[cal[i]] > stack[top]:
                stack[top] = cal[i]
                top += 1
            else:
                cal_2[k] = stack.pop(top-1)
                k += 1
    else:
        cal_2[k] = cal[i]
        k += 1
print(cal_2)
