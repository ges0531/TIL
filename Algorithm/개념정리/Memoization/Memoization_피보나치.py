def fib_memo(n, cache):
    # 코드를 작성하세요.
    if n == 1 or n == 2:
        return 1
    if n not in cache:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    else:
        return cache[n]
    return fib_memo(n-1, cache) + fib_memo(n-2, cache)


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


print(fib(10))
print(fib(50))
print(fib(100))