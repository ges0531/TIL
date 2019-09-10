import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    node_count = int(input())
    tree_list = [0] + list(map(int, input().split()))
    for i in range(1, (len(tree_list)//2)+1):
        b = i
        while i:
            if 2 * i < len(tree_list):
                if tree_list[i] > tree_list[2*i]:
                    tree_list[i], tree_list[2*i] = tree_list[2*i], tree_list[i]
            if 2 * i + 1 < len(tree_list):
                if tree_list[i] > tree_list[2*i+1]:
                    tree_list[i], tree_list[2 * i+1] = tree_list[2 * i+1], tree_list[i]
            i = i // 2
    a = (len(tree_list) - 1) // 2
    print(tree_list)
    my_sum = 0
    while a:
        my_sum += tree_list[a]
        a = a // 2
    print('#{} {}'.format(test_case, my_sum))