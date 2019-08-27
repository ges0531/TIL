s = []
def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return 0
    # underflow
    else:
        return s.pop()

def peek():
    if len(s) == 0:
        return
    else:
        return s[-1]

def IsEmpty():
    if len(s) == 0:
        return 'Empty'
    else:
        return 'Not Empty'
push(1)
print(s)
push(2)
print(s)
push(3)
print(s)
print(IsEmpty())
pop()
print(s)
print(peek())
pop()
print(s)
pop()
print(s)
IsEmpty()