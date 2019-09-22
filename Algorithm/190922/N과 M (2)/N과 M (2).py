import sys

sys.stdin = open('input.txt', 'r')

def combination(arr, r):
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == r:
            print(' '.join(map(str, chosen)))
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

num_1, num_2 = map(int, input().split())
num_list = [i+1 for i in range(num_1)]
combination(num_list, num_2)