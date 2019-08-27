def enQ(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = rear + 1
        Q[rear] = item


def deQ():
    global front
    if isEmpty():
        print('is_empty')
    else:
        front += 1
        return Q[front]


def isEmpty():
    return front == rear


def isFull():
    return rear == len(Q) - 1


def my_candy(a):
    global count, r1
    enQ(a)
    r1 += 1
    count -= r1
    deQ()
    enQ(a)
    print(count)


Q = [0] * 100
front = rear = -1
count = 20
i = 1
r1 = 0
while count != 0:
    input()
    print('Q in {}'.format(rear-front))
    input()
    print('cnady_count: {}'.format(i))
    input()
    print('give_candy: {}'.format(r1))
    my_candy(i)
    i += 1
print(i)