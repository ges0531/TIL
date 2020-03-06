A = [0, 4, 1, 3, 1, 2, 4, 1]
B = [0] * len(A)
C = [0] * len(set(A))

for i in range(0, len(B)):
    C[A[i]] += 1

for i in range(1, len(C)):
    C[i] += C[i-1]

for i in range(len(B)-1, -1, -1):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1

print(A, B, C)