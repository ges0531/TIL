import sys

sys.stdin = open('input.txt', 'r')


def perm(k):
    global my_min, min_location, min_location_2
    if k == N:
        my_sum = 0
        if location_2[0] == min_location and location_2[-1] == min_location_2:
            print(location_2)
            print(min_location, min_location_2)
            for g in range(len(location_2)-1):
                my_sum += abs(location_2[g][0]-location_2[g+1][0]) + abs(location_2[g][1]-location_2[g+1][1])
                if my_sum > my_min:
                    break
        if my_sum:
            if my_min > my_sum:
                my_min = my_sum
    else:
        for j in range(k, N):
            location_2[k], location_2[j] = location_2[j], location_2[k]
            perm(k+1)
            location_2[k], location_2[j] = location_2[j], location_2[k]


T = int(input())
T = 2
for test_case in range(1, T+1):

    customer_count = int(input())

    location = list(map(int, input().split()))
    home_location = [0, 0]
    work_location = [0, 0]
    location_2 = [0]*(customer_count)
    work_location[0] = location.pop(0)
    work_location[1] = location.pop(0)
    home_location[0] = location.pop(0)
    home_location[1] = location.pop(0)
    my_min = 10000
    min_value = 10000
    min_value_2 = 10000
    min_location = []
    min_location_2 = []
    a = 0
    b = 0
    for i in range(customer_count):
        location_2[i] = [location[2*i], location[2*i+1]]
    N = len(location_2)
    for short_track in range(len(location_2)):
        a = abs(location_2[short_track][0]-work_location[0])+abs(location_2[short_track][1]-work_location[1])
        if min_value > a:
            min_value = a
            min_location = location_2[short_track]
        b = abs(location_2[short_track][0]-home_location[0])+abs(location_2[short_track][1]-home_location[1])
        if location_2[short_track] != min_location:
            if min_value_2 > b:
                min_value_2 = b
                min_location_2 = location_2[short_track]
    perm(0)
    result_a = abs(min_location[0] - work_location[0]) + abs(min_location[1] - work_location[1])
    result_b = abs(min_location_2[0] - home_location[0]) + abs(min_location_2[1] - home_location[1])
    print(result_a, result_b)
    result_track = result_a+result_b+my_min
    print(my_min, 1)
    print('#{} {}'.format(test_case, result_track))