# testing cffi dot
from dotmod import lib
from cffi import FFI

ff = FFI()

a = [6,7,6]
b = [9,2,5]

# make c arrays
arr1 = ff.new("int[]", a)
arr2 = ff.new("int[]", b)

print(lib.dot_calc(arr1, arr2, len(a)))