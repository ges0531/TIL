import sys

sys.stdin = open('input.txt', 'r')


def permutation(arr, r):
    arr = sorted(arr)
    visited = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r:
            print(' '.join(map(str, chosen)))
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                visited[i] = 1
                generate(chosen, used)
                visited[i] = 0
                chosen.pop()

    generate([], visited)


num_1, num_2 = map(int, input().split())

num_list = [i+1 for i in range(num_1)]

permutation(num_list, num_2)