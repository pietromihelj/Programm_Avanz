from joblib import Parallel, delayed
import timeit

def f(x):
    res = 0
    for i in range(10000):
        res += i * x
    return res


n = 100

print([f(i) for i in range(n)])

print(Parallel(n_jobs=4)(delayed(f)(i) for i in range(n)))