import sys

sys.stdin = open('input.txt', 'r')


def BFS(v, visited, visited_2, queue):
    global count
    queue.append(v)
    visited_2[v] = 1
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            for j in relation[v]:
                if not visited[j]:
                    if not visited_2[j]:
                        visited_2[j] = visited_2[v]+1
                        queue.append(j)
                        if visited_2[j] <= 3:
                            count += 1


T = int(input())

for test_case in range(1, T+1):
    student_count, friends_count = map(int, input().split())
    friends_relation = [list(map(int, input().split())) for _ in range(friends_count)]
    friends_relation = sum(friends_relation, [])
    relation = [[] for _ in range(student_count+1)]
    for i in range(len(friends_relation)//2):
        relation[friends_relation[2*i]].append(friends_relation[2*i+1])
        relation[friends_relation[2 * i+1]].append(friends_relation[2 * i])
    count = 0
    BFS(1, [0]*(student_count+1), [0]*(student_count+1), [])
    print('#{} {}'.format(test_case, count))
