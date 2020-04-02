import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    B, C = map(int, input().split())
    H = list(map(int, input().split()))
    # ///////////////////////////////////////////////////////////////////////////////////
    my_max = my_min = sum(H[0:C])
    for i in range(B-C+1):
        my_sum = sum(H[i:i+C])
        if my_sum > my_max:
            my_max = my_sum
        if my_sum < my_min:
            my_min = my_sum
    result = my_max - my_min

    print('#%d %d' % (test_case, result))
