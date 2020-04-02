import sys

sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = 10

for test_case in range(1, T + 1):
    A = int(input())
    H = list(map(int, input().split()))
    # ///////////////////////////////////////////////////////////////////////////////////
    for j in range(A):
        H[H.index(max(H))] = max(H) - 1
        H[H.index(min(H))] = min(H) + 1
    result = max(H) - min(H)
    print('#%d %d' % (test_case, result))
