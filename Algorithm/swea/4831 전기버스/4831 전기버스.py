import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    print(A, B, C)
    H = list(map(int, input().split()))
    location = 0
    count = 0
    D = A
    # ///////////////////////////////////////////////////////////////////////////////////
    while location + A < B:
        if D == 0:
            count = 0
            break
        if location + D in H:
            location += D
            print(location)
            count += 1
            D = A
        else:
            D = D - 1

    print('#%d %d' % (test_case, count))