from functools import wraps
def wrap_function(f):
    def wrapped(*args,**kwargs):
        print("sto per chiamare f")
        x = f(*args,**kwargs)
        print("ho finito l'esecuzione di f")
        return x
    return wrapped
@wrap_function
def adder(x,y):
    return x+y

print(adder(3,4))

def logger(f):
    def add_logger(*args,**kwargs):
        with open("log.txt","a") as log:
            log.write(f"chiamo argomenti {args} e {kwargs}\n")
            x = f(*args,**kwargs)
            log.write(f"ottengo: {x} \n")
            return x
    return add_logger

@logger
def list_product(lst):
    somma = 0
    for i in lst:
        somma*=i
    return somma
list_product([1,2,3,4,5])

cache = {}
def cache_fun(f):
    name = f.__name__
    if name not in cache:
        cache[name] = {}
    @wraps(f)
    def whith_cache(x):
        if x in cache[name]:
            return cache[name][x]
        res = f(x)
        cache[name][x] = res
        return res
    return whith_cache

@cache_fun
def f(x):
    for i in range(100000000):
        x +=i
    return x

@logger
@cache_fun
def g(x):
    return -f(x)+2*x

print(f(10))
print(f(7))
print(f(10)-f(7))
print(g(10))
print(g(7))
print(g(10)-g(7))
print(cache)
print(f.__name__)