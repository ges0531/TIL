import sys

sys.stdin = open('input.txt', 'r')

def BFS(start_location):
    global result
    queue = [subin_location]
    visited = [0]*(bro_location+1)
    visited[subin_location] = 1
    while queue:
        a = queue.pop(0)
        b = a + 1
        if a * 2 <= 100000:
            c = a * 2
        if a - 1 >= 0:
            d = a - 1
        if c <= bro_location:
            if visited[c] == 0:
                visited[c] = visited[a] + 1
                queue.append(c)
        if b <= bro_location:
            if visited[b] == 0:
                visited[b] = visited[a] + 1
                queue.append(b)
        if d <= bro_location:
            if visited[d] == 0:
                visited[d] = visited[a] + 1
                queue.append(d)
    return visited[-1]-1


subin_location, bro_location = map(int, input().split())
result = 0
if subin_location == bro_location:
    print(0)
else:
    print(BFS(subin_location))

