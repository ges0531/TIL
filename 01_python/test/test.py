def binary_array_to_number(arr):
    my_sum = 0
    arr[0] = arr[0] * 1
    arr[1] = arr[1] * 2
    arr[2] = arr[2] * 5
    arr[3] = arr[3] * 8
    for num in arr:
        my_sum += arr[num]
        
    return my_sum

binary_array_to_number([0,1,1,1])
