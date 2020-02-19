import sys

sys.stdin = open('input.txt', 'r')


# 한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result

    if x == matrix_size:
        result += 1
        return

    for i in range(matrix_size):
        row[x] = i
        for j in range(x):
            if row[x] == row[j] or abs(row[x] - row[j]) == x - j:
                break
        else:
            dfs(x + 1)


matrix_size = int(input())
row = [0] * matrix_size
result = 0
dfs(0)
print(result)