def solution(p):
    int_p = p+1
    while True:
        str_p = str(int_p)
        for i in str_p:
            if str_p.count(i) >= 2:
                int_p += 1
                break
        else:
            return int(str_p)

print(solution(1987))