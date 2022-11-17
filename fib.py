import cfib
from time import perf_counter

def python_fib(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a

n = int(1e3)
print(n)
t1 = perf_counter()
x = python_fib(n)
t2 = perf_counter()
print(x)
t3 = perf_counter()
y = cfib.cython_fib(n)
t4 = perf_counter()
print(y)
print(t2-t1, t4-t3)

