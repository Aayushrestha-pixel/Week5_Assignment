# trying cython func
def rev_text(txt):
    cdef int i
    cdef int ln = len(txt)
    cdef list out = []   # store chars
    for i in range(ln-1, -1, -1):   # go backwards
        out.append(txt[i])
    return "".join(out)   # make string 