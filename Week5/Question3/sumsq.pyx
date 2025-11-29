# do sum of sq from 1..n
def sumsq(n):
    cdef long s = 0
    cdef int i
    for i in range(1, n+1):   # loop
        s += i * i            # square
    return s