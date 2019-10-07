import sys

sys.stdin = open('input.txt', 'r')

<<<<<<< HEAD
N = int(input())

num_list = [i+1 for i in range(N)]
a = [0]
index = 0
for _ in range(N-1):
    index += 1
    a[0] = num_list[index]
    index += 1
    num_list = num_list+a
print(num_list[-1])
=======
num_list = list(range(1, int(input())+1))
while len(num_list) > 1:
    num_list = num_list[2:] + [num_list[1]]
print(num_list[0])
>>>>>>> 3fb35b66cdaf0a66f1f5897005d8a7ae4dee17db
