import sys

sys.stdin = open('input.txt', 'r')


def perm(k):
    global result_location, last_location, my_min
    if k == N:
        my_sum = 0
        print(location_2)
        for g in range(len(location_2)-1):
            my_sum += abs(location_2[g][0]-location_2[g+1][0]) + abs(location_2[g][1]-location_2[g+1][1])
            last_location = location_2[-1]
        print(my_sum)
        if my_min > my_sum:
            my_min = my_sum
            result_location = last_location
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
    home_location = []
    location_2 = [0]*((len(location)//2)-1)
    home_location.append(location.pop(2))
    home_location.append(location.pop(2))
    my_min = 100000
    for i in range(len(location)//2):
        location_2[i] = [location[2*i], location[2*i+1]]
    N = len(location_2)
    last_location = [0]
    result_location = [0]
    # for h in range(len(location_2) - 1):
    #     my_min += abs(location_2[h][0] - location_2[h + 1][0]) + abs(location_2[h][1] - location_2[h + 1][1])
    perm(1)
    real_result = my_min + abs(result_location[0]-home_location[0])+abs(result_location[1]-home_location[1])
    print('#{} {}'.format(test_case, real_result))
