# fizz buzz => 3배수 fizz / 5배수 buzz / 15배수 fizzbuzz
number = int(input('숫자를 입력하세요: '))

for i in range(1, number + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
