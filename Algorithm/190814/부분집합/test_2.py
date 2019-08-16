arr = [1, 5, -9, 6, -2]
count = 0
my_list = []

for i in range(1, 1 << len(arr)):
    subset = []

    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == 0:
        my_list.append(subset)
        count += 1
print('합이 0이 되는 집합은 {}이고 개수는 {}개 입니다.'.format(my_list, count))