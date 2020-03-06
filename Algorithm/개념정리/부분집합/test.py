arr = [1, 5, -9, 6, -2]


for i in range(1, 1 << len(arr)):
    subset = []

    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])

    print(subset)