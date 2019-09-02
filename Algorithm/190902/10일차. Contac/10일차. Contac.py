import sys

sys.stdin = open('input.txt', 'r')

def BFS(E, v):
    visited = [0]*(my_max+1)
    queue = []
    queue.append(v)
    result = []
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
            result.append(t)
        for k in range(len(E[t])):
            if not visited[k]:
                if E[t][k] == 1:
                    visited[k] = visited[t] + 1
                    result.append(k)
                    queue.append(k)
    print(visited)
    return visited


T = 10

for test_case in range(1, T+1):
    data_length, start_node = map(int, input().split())
    contact_people = list(map(int, input().split()))
    my_max = max(contact_people)
    link_people = [0] * (len(contact_people)//2)
    G = [[0]*(my_max+1) for _ in range(my_max+1)]
    for i in range(len(contact_people)//2):
        link_people[i] = [contact_people[2*i], contact_people[2*i+1]]
    for column in range(len(link_people)):
        G[link_people[column][0]][link_people[column][1]] = 1
    finish = BFS(G, start_node)
    for last in range(len(finish)-1, 0, -1):
        if max(finish) == finish[last]:
            print('#{} {}'.format(test_case, last))
            break