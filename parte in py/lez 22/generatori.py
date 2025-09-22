def f():
    k = 1
    while True:
        yield k
        k += 1
        print(k)
    
def simple_generator():
    yield 1
    yield 2
    yield 3

def squares(n_elem):
    for n in range(n_elem):
        yield n**2

x = f()
while next(x) < 50:
    pass
    
y = simple_generator()
print(next(y))
print(next(y))
print(next(y))

s = squares(10)
for i in s:      #chiama square e assegna lo yield a i. termina quando riceve l'eccezione stop iteration
    print(i)