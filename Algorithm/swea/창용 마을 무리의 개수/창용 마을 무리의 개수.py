import sys

sys.stdin = open('input.txt', 'r')


def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())

for test_case in range(1, T+1):
    people_count, people_relation = map(int, input().split())
    relation = [list(map(int, input().split())) for _ in range(people_relation)]
    relation = sum(relation, [])
    relation_2 = [[] for _ in range(people_count+1)]
    count = 0
    for i in range(people_relation):
        relation_2[relation[2*i]].append(relation[2*i+1])
        relation_2[relation[2 * i+1]].append(relation[2 * i])
    p = [i for i in range(people_count+1)]
    for ii in range(len(p)):
        for jj in range(len(relation_2[ii])):
            union(ii, relation_2[ii][jj])
    for kk in range(len(p)):
        if p[kk] == kk:
            count += 1
    print('#{} {}'.format(test_case, count-1))