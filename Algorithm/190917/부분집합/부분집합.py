def power_set_r(k, N):
    c = []
    if k == N:
        for i in range(N):
            if a[i]*b[i]:
                c.append(a[i]*b[i])
        if sum(c) == 0:
            if c:
                print(c)
    else:
        a[k] = 1
        power_set_r(k + 1, N)
        a[k] = 0
        power_set_r(k + 1, N)

b = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
a = [0]*len(b)
power_set_r(0, len(a))
