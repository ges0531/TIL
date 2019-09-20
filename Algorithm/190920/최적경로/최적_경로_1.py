import sys

sys.stdin = open('input.txt', 'r')


def perm(k, n, result):
    global my_min, home_location
    if k == n:
        print(customer_location)
        if customer_location[-1] == home_location:
            my_sum = 0
            for l in range(len(customer_location)-1):
                my_sum += abs(customer_location[l][0]-customer_location[l+1][0])+abs(customer_location[l][1]-customer_location[l+1][1])
            if my_sum < my_min:
                my_min = my_sum
                my_min = result

    else:
        for ii in range(k, n):
            customer_location[k], customer_location[ii] = customer_location[ii], customer_location[k]
            # result += abs(customer_location[k][0] - customer_location[k-1][0]) + abs(customer_location[k][1] - customer_location[k-1][1])

            perm(k+1, n, result)
            # result -= abs(customer_location[k][0] - customer_location[k-1][0]) + abs(customer_location[k][1] - customer_location[k-1][1])
            customer_location[k], customer_location[ii] = customer_location[ii], customer_location[k]


T = int(input())
T= 1
for test_case in range(1, T+1):
    customer_count = int(input())
    location = list(map(int, input().split()))
    customer_location = [location[i:i+2] for i in range(0, len(location), 2)]
    home_location = customer_location[1]
    my_min = 1000000000000000
    perm(1, len(customer_location), 0)
    print(my_min)