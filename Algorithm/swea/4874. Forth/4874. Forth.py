import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    operater = ['+', '-', '*', '/', '.']
    calculater = input().split()
    stack = []
    for cal in calculater:
        if cal not in operater:
            stack.append(cal)
        elif cal == '.':
            if len(stack) == 1:
                print('#{} {}'.format(test_case, stack.pop()))
            else:
                print('#{} error'.format(test_case))
                break
        else:
            if len(stack) >= 2:
                if cal == '+':
                    num_1 = int(stack.pop())
                    num_2 = int(stack.pop())
                    result = num_2 + num_1
                    stack.append(result)
                elif cal == '-':
                    num_1 = int(stack.pop())
                    num_2 = int(stack.pop())
                    result = num_2 - num_1
                    stack.append(result)
                elif cal == '*':
                    num_1 = int(stack.pop())
                    num_2 = int(stack.pop())
                    result = num_2 * num_1
                    stack.append(result)
                elif cal == '/':
                    num_1 = int(stack.pop())
                    num_2 = int(stack.pop())
                    result = num_2 // num_1
                    stack.append(result)
            else:
                print('#{} error'.format(test_case))
                break



