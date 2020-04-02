

def permitution(arr, path, cur, visited):
    if len(path) == len(arr):
        print(path)
    else:
        for idx in range(len(arr)):
            if visited[idx] == 0:
                path.append(arr[idx])
                visited[idx] = 1
                permitution(arr, path, cur+1, visited)
                visited[idx] = 0
                path.pop()

numbers = list(range(1, 5))

permitution(numbers, [], 0, [0]*len(numbers))

