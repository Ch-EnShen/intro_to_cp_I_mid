import cfib
from time import perf_counter

def python_fib(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a

n = int(1e6)
t1 = perf_counter()
python_fib(n)
t2 = perf_counter()
cfib.cython_fib(n)
t3 = perf_counter()
print(t2-t1, t3-t2)

