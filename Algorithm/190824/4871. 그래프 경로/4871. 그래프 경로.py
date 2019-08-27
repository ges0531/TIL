import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    print(test_case, '-')
    node_num, link_num = map(int, input().split())
    link_box = [0] * link_num
    start_box = []
    for i in range(link_num):
        node_1, node_2 = map(int, input().split())
        link_box[i] = [node_1, node_2]
    first_node, second_node = map(int, input().split())
    print(link_box)



    # for start in link_box:
    #     if start[0] == first_node:
    #         start_box.append(start)
    # j = 0
    # count = 0
    # my_list = []
    # print(link_box)
    # for search in start_box:
    #     while j != len(link_box):
    #         for k in link_box:
    #             if search[1] == link_box[k][0]:
    #                 count += 1
    #         if count == 1:
    #             if search[1] == link_box[j][0]:
    #                 search[1] = link_box[j][1]
    #                 j = 0
    #             else:
    #                 j += 1
    #         else:
    #             for n in range(count):
    #                 my_list.append(search)
    #
    #
    # print(start_box)