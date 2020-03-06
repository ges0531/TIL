import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, 11):
   count = 0
   N = int(input())
   li = [list(map(int, input().split())) for _ in range(N)]
   stack = []
   for x in range(N):
       y = 0
       s = 0
       while y + s < 99:
           if li[y][x] == 1:
               for s in range(N-y):
                   if li[y+s][x] == 2:
                       count  += 1
                       y = y + s
                       break
           else:
               y += 1