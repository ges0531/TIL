def enQueue(item):
    global rear
    if isFull(): print('Queue_Full')
    else:
        rear = rear + 1
        Q[rear] = item


def deQueue():
    global front
    if isEmpty(): print('is_empty')
    else:
        front += 1
        return Q[front]


def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1

Q = [0] * 3
rear = front = -1
enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
print(Q)
print(deQueue())
print(deQueue())
print(deQueue())
deQueue()
print(Q)

