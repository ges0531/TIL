# def insert(idx, num, arr, length):
#     result = []
#     j = 0
#     for i in range(len(arr)+1):
#         if j == idx:
#             result.append(num)
#             idx = len(arr)+2
#         else:
#             result.append(arr[j])
#             j += 1
#     print(result)


def insert(idx, num, arr):
    arr += [0]
    for i in range(len(arr)-1, idx, -1):
        arr[i] = arr[i-1]
    arr[idx] = num

def erase(idx, arr):
    if idx == 0:
        arr.pop(0)
        return
    for j in range(idx+1, len(arr)):
        arr[j-1] = arr[j]
    arr.pop()


# insert test => arr.insert(위치, 삽입할 값)
arr = [10, 20, 30]
insert(3, 40, arr)
print(arr, len(arr))
insert(1, 50, arr)
print(arr, len(arr))
insert(0, 15, arr)
print(arr, len(arr))

# erase_test => arr.pop(위치)
arr = [10, 50, 40, 30, 70, 20]
erase(4, arr)
print(arr, len(arr))
erase(1, arr)
print(arr, len(arr))
erase(3, arr)
print(arr, len(arr))