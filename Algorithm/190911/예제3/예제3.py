n = 0x00111111
a = n & 0xff
print(0xff)
print(n)
if n & 0xff:
    print('little endian')
    print(a)
else:
    print('big endian')