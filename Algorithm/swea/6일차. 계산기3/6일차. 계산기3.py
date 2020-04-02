import sys


sys.stdin = open('input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    length = int(input())
    calculater = list(input())
    priority = {'+': 0, '*': 1}
    operater = ['+', '*', '(', ')']
    stack = []
    num = []
    for cal in calculater:
        if cal == '(':
            stack.append(cal)
        elif cal not in operater:
            num.append(cal)
        elif cal == ')':
            while num[-1] != '(':
                num.append(stack.pop())
            num.pop()
        elif cal == '*':
            stack.append(cal)
        elif cal == '+':
            if stack[-1] == '*':
                while stack[-1] == '*':
                    num.append(stack.pop())
                stack.append(cal)
            else:
                stack.append(cal)
    for cal_2 in num:
        if cal_2 not in operater:
            stack.append(cal_2)
        elif cal_2 == '*':
            num_1 = int(stack.pop())
            num_2 = int(stack.pop())
            result = num_2 * num_1
            stack.append(result)
        elif cal_2 == '+':
            num_1 = int(stack.pop())
            num_2 = int(stack.pop())
            result = num_2 + num_1
            stack.append(result)
    print('#{} {}'.format(test_case, result))

