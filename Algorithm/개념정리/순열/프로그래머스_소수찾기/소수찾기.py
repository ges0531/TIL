def solution(numbers):
    answer = 0
    a = list(str(numbers))
    result = []
    def prime_num(num):
        for k in range(2, num):
            if num % k == 0:
                return 0
        else:
            return 1

    def comb(n, r, arr, t):
        if r == 0:
            ans = int(''.join(t))
            prime = prime_num(ans)
            if (ans not in result) and (ans != 1) and prime and ans:
                result.append(ans)

        elif r > n:
            return
        else:
            t[r - 1] = arr[n - 1]
            comb(n - 1, r - 1, arr, t)
            comb(n - 1, r, arr, t)

    def perm(k, n, arr):
        if k == n:
            for ii in range(1, len(arr)+1):
                comb(len(arr), ii, arr, [0]*ii)
        else:
            for i in range(k, n):
                arr[i], arr[k] = arr[k], arr[i]
                perm(k+1, n, arr)
                arr[i], arr[k] = arr[k], arr[i]
    perm(0, len(a), a)
    return len(result)


print(solution('17'))