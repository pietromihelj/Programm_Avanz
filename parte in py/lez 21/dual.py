class Dual:

    def __init__(self, a, b):
        self.a = a #numero
        self.b = b #derivata

    def __add__(self, other):
        if isinstance(other, Dual):
            ra = self.a + other.a
            rb = self.b + other.b
        else:
            ra = self.a + other
            rb = self.b
        return Dual(ra, rb)

    def __sub__(self, other):
        if isinstance(other, Dual):
            ra = self.a - other.a
            rb = self.b - other.b
        else:
            ra = self.a - other
            rb = self.b
        return Dual(ra, rb)

    def __mul__(self, other):
        if isinstance(other, Dual):
            ra = self.a * other.a
            rb = self.a * other.b + self.b * other.a
        else:
            ra = self.a * other
            rb = self.b * other
        return Dual(ra, rb)
        
    def __str__(self):
        return f"{self.a} + {self.b}ε"

def f(x):
    if (x.a < 10):
        c1 = Dual(2,0)
        c2 = Dual(7,0)
        c3 = Dual(-1,0)
        return c1*x*x+c2*x+c3
    else:
        return x*x+x*x*x

def pot(x,y):
    for i in (range(y-1)):
        x = x*x
    return x

x = Dual(3,1)
c1 = Dual(2,0)
c2 = Dual(7,0)
c3 = Dual(-1,0)

print(pot(x,2))