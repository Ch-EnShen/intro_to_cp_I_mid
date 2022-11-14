import timeit
import cfib

def python_fib(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a

n = 1000
t1 = timeit.timeit(stmt = "python_fib(n)", setup = "def python_fib(n):;a, b = 0.0, 1.0;for i in range(n):;a, b = a + b, a;return a")
t2 = timeit.timeit(stmt = "cfib.cython_fib(n)")
print(t1, t2)

