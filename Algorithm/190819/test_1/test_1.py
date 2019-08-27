s = 'Reverse this strings'
for i in s[::-1]:
    print(i, end='')
print(' ')
print(''.join(reversed(s)))
s = s[::-1]
print(s)
