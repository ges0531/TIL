import sys

sys.stdin = open('input.txt', 'r')


def power_set_r(k):
    global ans
    result_list = [0]*num_count
    if k == num_count:
        for i in range(len(num_list)):
            result_list[i] = num_list[i]*a[i]
        if sum(result_list) not in ans:
            ans.append(sum(result_list))
    else:
        a[k] = 1
        power_set_r(k + 1)
        a[k] = 0
        power_set_r(k + 1)

T = int(input())

for test_case in range(1, T+1):
    num_count = int(input())
    num_list = list(map(int, input().split()))
    a = [0] * num_count
    ans = []
    power_set_r(0)
    print('#{} {}'.format(test_case, len(ans)))