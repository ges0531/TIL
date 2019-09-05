import sys

sys.stdin = open('input.txt', 'r')


def result(a, b):
    x = 0
    for i in range(1, a+1):
        x += i
        q = a
    for j in range(a, b+a-1):
        x += j

    return x


def location(z):
    k = 1
    g = 0
    my_list = []
    while g != z:
        f = 0
        for r in range(k):
            my_list.append(k)
            g += 1
            f += 1
            if g == z:
                break
        k += 1
    return [f, k-f]
T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    result_x = location(a)[0]+location(b)[0]
    result_y = location(a)[1]+location(b)[1]
    print('#{} {}'.format(test_case, result(result_x, result_y)))

