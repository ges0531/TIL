import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    B = int(input())
    H = list(map(int, input()))
    # ///////////////////////////////////////////////////////////////////////////////////
    my_dict = {}
    my_key = []
    for i in H:
        if i not in my_dict:
            my_dict[i] = H.count(i)
    for j in my_dict:
        if my_dict[j] == max(my_dict.values()):
            my_key.append(j)
    print('#%d %d %d' % (test_case, max(my_key), my_dict[max(my_key)]))