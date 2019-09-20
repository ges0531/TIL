import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n):
    global my_min
    if k == n:
        my_sum = 0
        if customer_location[0] == work_min:
            if customer_location[-1] == home_min:
                for l in range(len(customer_location)-1):
                    my_sum += abs(customer_location[l][0]-customer_location[l+1][0])+abs(customer_location[l][1]-customer_location[l+1][1])
                if my_sum < my_min:
                    my_min = my_sum
    else:
        for ii in range(k, n):
            customer_location[k], customer_location[ii] = customer_location[ii], customer_location[k]
            perm(k+1, n)
            customer_location[k], customer_location[ii] = customer_location[ii], customer_location[k]


T = int(input())
T = 3
for test_case in range(1, T+1):
    print(test_case)
    customer_count = int(input())
    location = list(map(int, input().split()))
    work_location = []
    home_location = []
    work_location.append(location.pop(0))
    work_location.append(location.pop(0))
    home_location.append(location.pop(0))
    home_location.append(location.pop(0))
    customer_location = [location[i:i+2] for i in range(0, len(location), 2)]
    my_min_1 = 100000000000000
    my_min_2 = 100000000000000
    my_min = 1000000000000000
    work_min = []
    home_min = []
    for j in range(len(customer_location)):
        min_1 = abs(work_location[0]-customer_location[j][0]) + abs(work_location[1] - customer_location[j][1])
        if min_1 < my_min_1:
            my_min_1 = min_1
            work_min = customer_location[j]
    for jj in range(len(customer_location)):
        if customer_location[jj] != work_min:
            min_2 = abs(home_location[0] - customer_location[jj][0]) + abs(home_location[1] - customer_location[jj][1])
            if min_2 < my_min_2:
                my_min_2 = min_2
                home_min = customer_location[jj]
    perm(0, len(customer_location))
    print(my_min+my_min_1+my_min_2)