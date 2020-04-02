cal = '2+3*4/5'
cal = list(cal)
operator = ['+', '-', '*', '/']
stack = [0] * 3
top = 0
for i in range(len(cal)):
    if cal[i] not in operator:
        print(cal[i],end='')
    else:
        stack[top] = cal[i]
        top += 1
else:
    for j in range(len(stack)):
        print(stack.pop(), end='')
