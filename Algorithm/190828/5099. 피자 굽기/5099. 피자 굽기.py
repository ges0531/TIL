import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    size, pizza_count = map(int, input().split())
    pizza = list(map(int, input().split()))
    count = 0
    baked_pizza = [pizza.pop(0) for _ in range(size)]
    pizza_index = [0] * pizza_count
    for i in range(pizza_count):
        pizza_index[i] = i+1
    baked_pizza_index = [pizza_index.pop(0) for _ in range(size)]
    while baked_pizza.count(0) != size:
        a = baked_pizza.pop(0)
        b = baked_pizza_index.pop(0)
        if count >= size:
            a = a//2
        if a == 0 and pizza:
            baked_pizza.append(pizza.pop(0))
            baked_pizza_index.append(pizza_index.pop(0))
        else:
            baked_pizza.append(a)
            baked_pizza_index.append(b)
        count += 1
    print('#{} {}'.format(test_case, baked_pizza_index[-1]))
