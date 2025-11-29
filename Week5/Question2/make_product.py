# cffi build file
from cffi import FFI
ff = FFI()

# tell python the c function
ff.cdef("int dot_calc(int *a, int *b, int n);")

# read c file
src = open("dot.c").read()

ff.set_source("dotmod", src)

ff.compile()