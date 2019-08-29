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





Q = [0] * 100
front = rear = -1
count = 20
student = [1] * 20
sn = 1
nextsn = 2

rear += 1
Q[r] = sn

while count != 0:
    front += 1:
    sn = Q[front]
    candis -= student[sn]
    student[sn] += 1

    if candis <= 0:
        print('{}번 학생이 마지막 사탕을 받아간다.'.format(sn))
        break
    rear += 1
    Q[rear] = sn
    rear += 1
    Q[rear] = sn