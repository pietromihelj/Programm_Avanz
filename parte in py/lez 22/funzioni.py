def make_adder(x):
    def g(y):
        return x+y
    return g
plus_five = make_adder(5)
plus_ten = make_adder(10)
print(plus_five(3))
print(plus_ten(3))


def mapf(f):
    def g(lst):
        return [f(x) for x in lst]
    return g
sum_5_to_list = mapf(plus_five)
list = [3,4,5,6,7,8,9,10]
print(sum_5_to_list(list))


def valuta_parziale(f,x):
    def g(y):
        return f(x,y)
    return g
def somma(x,y):
    return x+y
h = valuta_parziale(somma,6)
print(h(10))


def f(x):
    def g (y):
        def h(z):
            return x+y+z
        return h
    return g
print(f(7)(8)(10))

def funzioni_in_sequenza(flist,x):
    for f in flist:
        x = f(x)
    return x
flist = [plus_five,plus_ten,make_adder(20)]
print(funzioni_in_sequenza(flist, 7))