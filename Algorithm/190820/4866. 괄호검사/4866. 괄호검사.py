import sys


sys.stdin = open('input.txt', 'r')

T = int(input())

s = []
def push(item):
    s.append(item)

def pop():
    if s == []:
        return
    else:
        return s.pop()

for test_case in range(1, T+1):
    string = input()
    if string.count('(') == string.count(')') and  string.count('{') == string.count('}'):
        for i in string:
            if i == '(' or i == '{':
                push(i)
            if i == ')':
                if len(s) == 0:
                    print('#{} {}'.format(test_case, 0))
                    break
                else:
                    if s[-1] == '(':
                        pop()
                    elif s[-1] != '(':
                        print('#{} {}'.format(test_case, 0))
                        break
            if i == '}':
                if len(s) == 0:
                    print('#{} {}'.format(test_case, 0))
                    break
                else:
                    if s[-1] == '{':
                        pop()
                    elif s[-1] != '{':
                        print('#{} {}'.format(test_case, 0))
                        break
        else:
            print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))

    # if s == []:
    #     print('#{} {}'.format(test_case, 1))
    # else:
    #     print('#{} {}'.format(test_case, 0))
