import sys

sys.stdin = open('input.txt', 'r')


def preorder_traverse(T):
    if T:
        try:
            preorder_traverse(result[T][0])
            print(T, end=' ')
            preorder_traverse(result[T][1])
        except IndexError:
            pass
node_count = int(input())
tree_list = list(map(int, input().split()))

pre_list = [0]*(len(tree_list)//2)
result = []
for i in range((len(tree_list)//2)):
    pre_list[i] = [tree_list[2*i], tree_list[2*i+1]]
for k in range(node_count):
    middle = [0]*2
    index = 0
    for j in range(len(pre_list)):
        if pre_list[j][0] == k:
            middle[index] = pre_list[j][1]
            index += 1
    for kk in range(len(middle)):
        if middle[kk-1] == 0:
            middle.pop()
    result.append(middle)
print(result)
preorder_traverse(1)
