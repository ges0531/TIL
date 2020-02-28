def fib_optimized(n):
    # 코드를 작성하세요.
    currnet = previous = 1
    temp = 0
    for i in range(3, n+1):
        temp = currnet
        currnet += previous
        previous = temp
    return currnet

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
