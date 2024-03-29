import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)

    slist = list(input().split())
    dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    count = [0]*10

    for i in range(N):
        count[dict[slist[i]]] += 1

    str = ""
    temp = list(dict.keys())
    for i in range(10):
        for _ in range(count[i]):
            str += temp[i]
            str += " "
    print("%s %s" % (tc,str))