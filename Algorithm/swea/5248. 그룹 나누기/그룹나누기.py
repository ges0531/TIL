import sys

sys.stdin = open('input.txt', 'r')


def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())

for test_case in range(1, T+1):
    student_count, application_count = map(int, input().split())
    application = list(map(int, input().split()))
    my_list = [0 for _ in range(student_count+1)]
    result = []
    count = 0
    for j in range(len(application)):
        my_list[application[j]] += 1
    application_2 = [[] for _ in range(student_count+1)]
    for i in range(application_count):
        application_2[application[2*i]].append(application[2*i+1])
        application_2[application[2 * i+1]].append(application[2 * i])
    p = [k for k in range(student_count+1)]
    for ii in range(len(application_2)):
        for jj in range(len(application_2[ii])):
            union(ii, application_2[ii][jj])
    for kk in range(len(p)):
        if kk == p[kk]:
            count += 1
    print('#{} {}'.format(test_case, count-1))