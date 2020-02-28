def fib_tab(n):
    table = {1: 1, 2: 1}
    for i in range(1, n+1):
        if i not in table:
            table[i] = table[i-1] + table[i-2]
    return table[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))