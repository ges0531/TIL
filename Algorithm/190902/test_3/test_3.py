def enQ(x):
    q.append(x)

def deQ():
    small_num = q[0]
    for i in range(len(q)):
        if q[i] < small_num:
            small_num = q[i]
    return q.pop(q.index(small_num))

q = []

enQ(1)
enQ(5)
enQ(2)
enQ(4)
enQ(3)
print(q)
print(deQ())
print(q)
print(deQ())
print(q)
print(deQ())
print(q)
print(deQ())
print(q)
print(deQ())


