import sys

sys.stdin = open('input.txt', 'r')


def preorder_traverse_1(T):
    if T:
        try:
            preorder_traverse_1(link_node[T][0])
        except IndexError:
            pass
        print(T, end=' ')
        try:
            preorder_traverse_1(link_node[T][1])
        except IndexError:
            pass


def preorder_traverse_2(T):
    print(T, end=' ')
    if T:
        try:
            preorder_traverse_2(link_node[T][0])
            preorder_traverse_2(link_node[T][1])
        except IndexError:
            pass


def preorder_traverse_3(T):
    if T:
        try:
            preorder_traverse_3(link_node[T][0])
            preorder_traverse_3(link_node[T][1])
        except IndexError:
            pass
        print(T, end=' ')


node_count = int(input())
node_link = list(map(int, input().split()))
link_node = [[] for _ in range(node_count+1)]
for i in range(len(node_link)//2):
    link_node[node_link[2*i]].append(node_link[2*i+1])
print(link_node)
preorder_traverse_1(1)
print()
preorder_traverse_2(1)
print()
preorder_traverse_3(1)
