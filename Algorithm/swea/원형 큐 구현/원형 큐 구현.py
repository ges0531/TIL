def isEmpty():
    return front == rear


def isFull():
    return (rear+1) % len(cQ) == front


def enQ(item):
    global rear
    if isFull():
        print("Queue_Full")
        