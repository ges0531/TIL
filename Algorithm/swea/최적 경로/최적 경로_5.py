import sys

sys.stdin = open('input.txt', 'r')


def perm(k):
    global my_min
    if k == N:
        if location[-1] == home_location[1] and location[-2] == home_location[0]:
            my_sum = 0
            for g in range(len(location)):
                my_sum += abs(location[2*g][0]-location[2*g+2][0]) + abs(location[2*g+1][1]-location[2*g+3][1])
                if my_sum >= my_min:
                    break
            if my_sum:
                if my_min > my_sum:
                    my_min = my_sum
    else:
        for j in range(k, N):
            location[k], location[j] = location[j], location[k]
            perm(k+1)
            location[k], location[j] = location[j], location[k]


T = int(input())
for test_case in range(1, T+1):

    customer_count = int(input())

    location = list(map(int, input().split()))
    home_location = [0, 0]
    # location_2 = [0]*(len(location)//2)
    home_location[0] = location[2]
    home_location[1] = location[3]
    my_min = 10000
    # for i in range(len(location)//2):
    #     location_2[i] = [location[2*i], location[2*i+1]]
    N = len(location)
    perm(1)
    print('#{} {}'.format(test_case, my_min))