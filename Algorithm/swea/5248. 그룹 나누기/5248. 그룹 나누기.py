import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    student_count, application_count = map(int, input().split())
    application = list(map(int, input().split()))
    my_list = [0 for _ in range(student_count+1)]
    for j in range(len(application)):
        my_list[application[j]] += 1
    application_2 = [[] for _ in range(student_count+1)]
    application_3 = [0 for _ in range(student_count+1)]
    a = 0
    b = 0
    c = 0
    for i in range(application_count):
        application_2[application[2*i]].append(application[2*i+1])
        application_2[application[2 * i+1]].append(application[2 * i])
    for ii in range(len(application_2)):
        if application_2[ii] == []:
            b += 1
    for k in range(len(my_list)):
        if my_list[k] > 1:
            for kk in application_2[k]:
                application_2[kk] = []
            application_2[k] = []
            a += 1
    for m in range(len(application_2)):
        if application_2[m]:
            c += 1

    print('#{} {}'.format(test_case, a+(b-1)+(c//2)))




