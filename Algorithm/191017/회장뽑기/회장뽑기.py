import sys

sys.stdin = open('input.txt', 'r')


def BFS(start_node, n, G):
    global my_min
    queue = [start_node]
    visited = [0]*(n+1)
    visited[start_node] = 1
    while queue:
        a = queue.pop(0)
        for ii in range(len(G[a])):
            if not visited[G[a][ii]]:
                queue.append(G[a][ii])
                visited[G[a][ii]] = visited[a]+1
    my_num = max(visited)-1
    if my_min > my_num:
        my_min = my_num
    return my_num


people_count = int(input())
vote_list = []
while 1:
    a = list(map(int, input().split()))
    if a != [-1, -1]:
        vote_list.append(a)
    else:
        break
G = [[] for _ in range(people_count+1)]
my_min = 100000000
real_result = []
my_list = []
for i in range(len(vote_list)):
    G[vote_list[i][0]].append(vote_list[i][1])
    G[vote_list[i][1]].append(vote_list[i][0])

for j in range(1, people_count+1):
    real_result.append(BFS(j, people_count, G))
for jj in range(len(real_result)):
    if my_min == real_result[jj]:
        my_list.append(jj+1)

my_list.sort()
print(my_min, len(my_list))
for k in my_list:
    print(k, end=' ')
