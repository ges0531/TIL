import sys

sys.stdin = open('input.txt', 'r')

room_count = int(input())

meeting_room = [list(map(int, input().split())) for _ in range(room_count)]
meeting_room.sort()
meeting_room.sort(key=lambda x: x[1])
count = 1
a = meeting_room[0][1]
for i in range(1, room_count):
    if meeting_room[i][0] >= a:
        a = meeting_room[i][1]
        count += 1
print(count)