def backtrack(a, k, input):
    global MAXCABDIDATES
    c = [0] * MAXCABDIDATES

    if k == input:
        if sum(a) == 10:
            for i in range(1, k+1):
                print(a[i], end=' ')
            print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

MAXCABDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 10)