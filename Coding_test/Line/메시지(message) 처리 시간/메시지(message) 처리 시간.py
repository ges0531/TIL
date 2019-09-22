import sys

sys.stdin = open('input.txt')
message_count, consumer_count = map(int, input().split())

message_time = [int(input()) for _ in range(message_count)]
consumer = [[0] for _ in range(consumer_count)]
my_min = sum(message_time)
my_max = 0
for i in range(message_count):
    index = 0
    if i == 0:
        consumer[i].append(message_time[i])
    else:
        for j in range(consumer_count):
            for k in range(consumer_count):
                if j != k:
                    if sum(consumer[j]) < sum(consumer[k]):
                        index = j
        consumer[index].append(message_time[i])

for m in range(consumer_count):
    if sum(consumer[m]) > my_max:
        my_max = sum(consumer[m])
print(my_max)
