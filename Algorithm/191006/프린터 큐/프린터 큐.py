import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    text_count, find_text = map(int, input().split())
    text_list = list(map(int, input().split()))
    index_list = [k for k in range(text_count)]
    count = 0
    b = 100000000000000
    while b != find_text:
        a = 0
        for i in range(1, len(text_list)):
            if text_list[0] < text_list[i]:
                a = 1
                break
        if a == 1:
            text_list.append(text_list.pop(0))
            index_list.append(index_list.pop(0))
        else:
            text_list.pop(0)
            b = index_list.pop(0)
            count += 1
    print(count)