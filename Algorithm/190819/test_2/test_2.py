def atoi(str):
    value = 0

    for i in range(len(str)):
        if ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
            digit = ord(str[i]) - ord('0')
        else:
            break

        value = (value * 10) + digit
    return value

print(atoi('123'))


def myitoa(x):
    sr = ''
    while True:
        r = x % 10  # 3, 2, 1
        sr = sr + chr(r + ord('0'))
        x //= 10
        if x == 0:
            break

    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s = s + sr[i]
    return s


print(myitoa(123))
