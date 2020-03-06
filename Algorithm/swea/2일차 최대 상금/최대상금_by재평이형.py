import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T + 1):
    tmp = list(map(int, input().split()))
    numbers = list(map(int, str(tmp[0])))
    max_change = tmp[1]

    max_numbers = list(reversed(sorted(numbers)))

    count = 0
    for i in range(len(numbers)):
        if numbers[i] != max_numbers[i]:
            count += 1

    tmp_change = (count + 1) // 2

    if tmp_change <= max_change:
        if (max_change - tmp_change) % 2 and len(set(max_numbers)) == len(max_numbers):
            max_numbers[-1], max_numbers[-2] = max_numbers[-2], max_numbers[-1]

        result = ''.join(map(str, max_numbers))
    else:
        cnt, recur = 0, 0
        while cnt < max_change:
            max_number, max_idx = -1, 0
            for idx in range(recur, len(numbers)):
                if max_number < numbers[idx]:
                    max_number = numbers[idx]
                    max_idx = idx
                elif max_number == numbers[idx]:
                    max_idx = idx

            if max_idx != recur:
                numbers[max_idx], numbers[recur] = numbers[recur], numbers[max_idx]
                cnt += 1
                recur += 1
            else:
                recur += 1
        result = ''.join(map(str, numbers))

    print('#{} {}'.format(t, result))