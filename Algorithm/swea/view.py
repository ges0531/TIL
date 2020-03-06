import sys
sys.stdin = open("input.txt", "r")


T = 10

# T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))

    my_sum = 0
    count = 0
    for i in H[2:]:
        if H[count] > max(H[count-2], H[count-1], H[count+1], H[count+2]):
            my_sum += H[count] - max(H[count-2], H[count-1], H[count+1], H[count+2])
        count += 1
    print('#%d %d' % (test_case, my_sum))