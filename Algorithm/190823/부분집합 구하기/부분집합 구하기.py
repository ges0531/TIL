def backtrack(a, k, input):
    global MAXCABDIDATES
    c = [0] * MAXCABDIDATES
    my_box = [0]*(input+1)
    if k == input:
        for i in range(1, k+1):
            my_box[i] = a[i]
        print(my_box)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2


MAXCABDIDATES = 100
NMAX = 100
a = [0] * NMAX
print(backtrack(a, 0, 10))
