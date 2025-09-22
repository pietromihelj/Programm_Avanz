f = lambda x: x+2
print(f(2))

g = lambda x, y: x+y+3
print(g(3,4))

h = lambda f,x: f(x)
print(h(f,3))

y = h(lambda x: x**2,5) #apply
print(y)

compose=lambda f,g: (lambda x: g(f(x)))
sqr_3 = compose(lambda x: x**2, lambda x:x+3)
print(sqr_3(4))

def calcolo_lungo(n):
    m=0
    for i in range(n**n):
        m+=1
    return m
x = lambda:calcolo_lungo(8)

def esegui_if(cond,a,b):
    if cond:
        return a
    else:
        return b
esegui_if(4<10, lambda: 4, lambda: calcolo_lungo(10))


