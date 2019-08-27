def BruteForce(p, t):
    i = 0
    j = 0
    M = len(p)
    N = len(t)
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M
    else:
        return -1
a = 'a pattern matching algorithm'
b = 'rithm'


print(BruteForce(b, a))