import sys

sys.stdin = open('input.txt', 'r')


def make_k(start_node, k):
    a = k
    b = 0
    count = 0
    for j in range(k):
        for i in range(-a+1, a):
            if 0 <= start_node[0]+b < size and 0 <= start_node[1]+i < size:
                if matrix[start_node[0]+b][start_node[1]+i]:
                    count += 1
            if 0 <= start_node[0] - b < size and 0 <= start_node[1] + i < size:
                if matrix[start_node[0]-b][start_node[1]+i]:
                    if b:
                        count += 1
        a -= 1
        b += 1
    return count



T = int(input())
# T = 1
for test_case in range(1, T + 1):
    size, home_cost = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    k = 1
    my_max = 0
    while k <= size+2:
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                result = make_k([row, column], k)
                if (home_cost*result) - ((k**2)+((k-1)**2)) >= 0:
                    if my_max < result:
                        my_max = result
        k += 1
    print('#{} {}'.format(test_case, my_max))
