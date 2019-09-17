# nCr = (n-1)C(r-1) + (n-1)Cr (n >= r)
# nC0 = 1 -> 재귀에서 베이스 파트
# 또는 n과 r이 같아지는 시기에 종료
# an[]: n개의 원소를 가지고 있는 배열
# tr[]: r개의 크기의 배열, 조합이 임시 저장될 배열

def comb(n, r):
    if r == 0:
        if sum(tr) == 0:
            if tr:
                print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
an = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
for i in range(len(an)):
    tr = [0] * i
    comb(len(an), len(tr))