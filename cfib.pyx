# cython: language_level=3
cimport cython

cpdef int cython_fib(int n):
    cdef int i
    cdef int a = 0, b = 1
    for i in range(n):
        a, b = a + b, a
    return a
