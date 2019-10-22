import sys
import collections

sys.stdin = open('input.txt', 'r')

def BFS(start_location):
    global result
    queue = collections.deque()
    queue.append(subin_location)
    visited = [0]*100001
    visited[subin_location] = 1
    while queue:
        a = queue.popleft()
        b = a + 1
        c = a * 2
        d = a - 1
        if c <= 100000:
            if visited[c] == 0:
                visited[c] = visited[a] + 1
                queue.append(c)
        if b <= 100000:
            if visited[b] == 0:
                visited[b] = visited[a] + 1
                queue.append(b)
        if d >= 0:
            if visited[d] == 0:
                visited[d] = visited[a] + 1
                queue.append(d)
    return visited[bro_location]-1


subin_location, bro_location = map(int, input().split())
result = 0
if subin_location == bro_location:
    print(0)
else:
    print(BFS(subin_location))

