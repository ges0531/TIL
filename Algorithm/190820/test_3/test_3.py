arr = [0] * 8
my_list = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
num_set = [0] * 8
# for i in range(len(my_list)//2):
#     num_set[i] = [my_list[2*i], my_list[2 * i + 1]]
#

for i in range(8):
    arr[i] = [0] * 8


for i in range(0, len(my_list), 2):
    arr[my_list[i]][my_list[i+1]] = 1
    arr[my_list[i+1]][my_list[i]] = 1
print(arr)

def DFS(v):
    visited = stack = [0] * 8
    for j in arr[v]:
        if j == 1:
            visited[v] = 1
            stack[v] = v
            break
    while stack != []:
        v = stack.pop()
        while
