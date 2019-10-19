import sys
sys.stdin = open('input.txt', 'r')

def link(x):
    if arr[x]:          # 연결 점이 있다면
        for idx in range(len(arr[x])):    # 점을 돌면서 확인하라
            if not visited[arr[x][idx][1]]:   # 이미 연결점을 확인한 곳이 아니라면
                if key[arr[x][idx][1]] == 0 and pi[arr[x][idx][1]] == 0:   # 아무 것도 연결되지 않은 점이라면 그냥 값을 채워줘
                    key[arr[x][idx][1]] = arr[x][idx][0]
                    pi[arr[x][idx][1]] = x
                elif key[arr[x][idx][1]]:                                   # 이미 값이 존재한다면 새로 넣으려고 했던 값과 원래 값 중 더 작은 값을 넣어줘
                    if key[arr[x][idx][1]] > arr[x][idx][0]:
                        key[arr[x][idx][1]] = arr[x][idx][0]
                        pi[arr[x][idx][1]] = x
        visited[x] = 1                               # 연결점 확인 끝났다면 여기는 다시 안오게 체크해줘
        for i in range(len(arr[x])):                 # 다음으로 작은애부터 확인 안한 점으로 이동해
            if not visited[arr[x][i][1]]:
                link(arr[x][i][1])
N = int(input())
point = [num for num in range(N+1)]
arr = [[] for _ in range(N+1)]  # arr 에 가중치와 정점 넣기
key = [0] * (N+1)   # 가중치 list
pi = [0] * (N+1)    # 정점 list
visited = [0] * (N+1)
while True:
    a, b, v = map(int, input().split())
    if a == -1:
        break
    arr[a].append([v, b])
    arr[b].append([v, a])

for ali in range(N+1):   # 가중치로 sort 되어 정점 연결 시 가장 작은애부터 들어가게 됨
    arr[ali].sort()
visited[0] = 1
link(0)
print(key, pi)