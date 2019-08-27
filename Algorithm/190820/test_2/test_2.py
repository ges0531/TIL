s = []
def push(item):
    s.append(item)

def pop():
    if s == 0:
        return
    else:
        return s.pop()
def test(x):
    for i in x:
        if i == '(':
            push(i)
        elif i == ')':
            pop()
    if s == []:
        return 'is right'
    else:
        return 'Error'

a = '()()((()))'
b = '((()((((()()((()())((())))))'

print(test(a))
print(test(b))
