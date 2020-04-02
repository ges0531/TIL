import sys


sys.stdin = open('input.txt', 'r')

T = 10


def BFS(E, v):
    visited = [0]*(my_max+1)
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
        for k in range(len(E[t])):
            if not visited[k]:
                if E[t][k] == 1:
                    visited[k] = visited[t] + 1
                    queue.append(k)
    for finish in range(len(visited)-1, 0, -1):
        if max(visited) == visited[finish]:
            print('#{} {}'.format(test_case, finish))
            break


for test_case in range(1, T+1):
    data_length, start_node = map(int, input().split())
    contact = list(map(int, input().split()))
    contacts = [0]*(len(contact)//2-1)
    my_max = max(contact)
    matrix = [[0]*(my_max+1) for _ in range(my_max+1)]
    for i in range((len(contact)//2)-1):
        contacts[i] = [contact[2*i], contact[2*i+1]]
    # for i in range(len(contacts)):
    #     for j in range(i+1, len(contacts)):
    #         if contacts[i] == contacts[j]:
    #             contacts[j] = [0, 0]
    for column in range(len(contacts)):
        matrix[contacts[column][0]][contacts[column][1]] = 1
    BFS(matrix, start_node)
