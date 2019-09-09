import sys

sys.stdin = open('input.txt', 'r')


def perm(k):
    global a
    if k == N:
        if result[a] != location_2[0] + location_2[1]:
            result.append(location_2[0] + location_2[1])
            a += 1
    else:
        for j in range(k, N):
            location_2[k], location_2[j] = location_2[j], location_2[k]
            perm(k+1)
            location_2[k], location_2[j] = location_2[j], location_2[k]

T = int(input())
T = 1

for test_case in range(1, T+1):

    customer_count = int(input())

    location = list(map(int, input().split()))
    home_location = []
    location_2 = [0]*((len(location)//2)-1)
    home_location.append(location.pop(2))
    home_location.append(location.pop(2))
    for i in range(len(location)//2):
        location_2[i] = [location[2*i], location[2*i+1]]
    N = len(location_2)
    result = [0]
    result_3 = []
    a = 0
    perm(0)
    result.pop(0)
    for ii in range(len(result)):
        for jj in range(ii, len(result[0])):
            if set(result[ii]) == set(result[jj]):
                result[jj] = []

    print(result)
    for loc in range(len(location_2)):
        result_2 = []
        for res in range(len(result)):
            if result[res] != []:
                if location_2[loc][0] == result[res][0] and location_2[loc][1] == result[res][1]:
                    result_2.append(abs(result[res][2]-result[res][0])+abs(result[res][3]-result[res][1]))
        result_3.append(result_2)
    print(result_3)