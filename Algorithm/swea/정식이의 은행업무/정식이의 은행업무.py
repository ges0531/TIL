import sys

sys.stdin = open('input.txt', 'r')



T = int(input())

for test_case in range(1, T+1):
    binary_num = input()
    tetra_num = input()
    a = 0
    d = 0
    result = 0
    e = 0
    f = 0
    z = 0
    result_2 = 0
    real_result = []
    real_result_2 = []
    for j in range(len(binary_num)-1, -1, -1):
        result += int(binary_num[j]) * (2 ** d)
        d += 1
    for i in range(len(binary_num)-1, -1, -1):
        c = 0
        b = 0
        if int(binary_num[i]) == 0:
            b = (2 ** a)
        else:
            c = (2 ** a)
        a += 1
        real_result.append(result + b - c)

    for k in range(len(tetra_num)-1, -1, -1):
        result_2 += int(tetra_num[k]) * (3 ** e)
        e += 1
    for g in range(len(tetra_num)-1, -1, -1):
        c = 0
        b = 0
        if int(tetra_num[g]):
            c = int(tetra_num[g]) * (3 ** f)
        else:
            b = (3 ** f)
        f += 1
        real_result_2.append(result_2 + b - c)
    for h in range(len(tetra_num)-1, -1, -1):
        c = 0
        b = 0
        cc = 0
        if int(tetra_num[h]) == 2:
            c = (3 ** z)
        elif int(tetra_num[h]) == 1:
            cc = (3 ** z)
        else:
            b = (3 ** z) * 2
        z += 1
        real_result_2.append(result_2 + b + cc - c)
    for same in range(len(real_result)):
        for same_2 in range(len(real_result_2)):
            if real_result[same] == real_result_2[same_2]:
                print('#{} {}'.format(test_case, real_result[same]))
                break