import sys

sys.stdin = open('input.txt', 'r')

def count_diff(a, b):
    count = 0
    for ii in range(len(a)):
        if a[ii] != b[ii]:
            count += 1
    return count


A, B = input().split()
diff_len = len(B) - len(A)
my_min = 51
for i in range(diff_len+1):
    result = count_diff(A, B[i:len(A)+i+1])
    if result < my_min:
        my_min = result
print(my_min)
