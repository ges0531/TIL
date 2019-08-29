def enQ(item):
    global rear
    if isFull():
        print('Queue is Full')
    else:
        rear += 1
        Q[rear] = item


def deQ():
    global front
    if isEmpty():
        print('Empty')
    else:
        front += 1
        return Q[front]


def isFull():
    return rear == len(Q) - 1


def isEmpty():
    return front == rear


def BFS(E, v):
    visited = [0]*8
    queue = []
    queue.append(v)
    result = []
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            result.append(t)
        for k in range(len(E[t])):
            if not visited[k]:
                if E[t][k] == 1:
                    queue.append(k)
    return result


G = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
A = [[0] * 8 for _ in range(8)]
my_box = [0] * (len(G)//2)
for i in range(len(G)//2):
    my_box[i] = [G[2*i], G[2*i+1]]
for j in range(8):
    A[my_box[j][0]][my_box[j][1]] = 1
    A[my_box[j][1]][my_box[j][0]] = 1


print(BFS(A, 1))




