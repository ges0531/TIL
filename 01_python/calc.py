# 1번 - teacher

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return '0으로 나눌 수 없음.'