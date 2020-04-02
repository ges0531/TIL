import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    print('#{}'.format(test_case))
    pascal_count = int(input())
    nums = [1, 1]
    if pascal_count == 1:
        print(1)
    else:
        print(1)
        print(' '.join(map(str, nums)))
        for pascal in range(3, pascal_count+1):
            i = 0
            result = []
            for num in range(pascal-2):
                result.append(nums[i] + nums[i+1])
                i += 1
            nums = [1] + result + [1]
            print(' '.join(map(str, nums)))
