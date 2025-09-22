from collections import defaultdict
import copy

class Polynomial:
  def __init__(self, coeffs):
     self.__poly = defaultdict(int) 
     for k in coeffs:
       self.__poly[k] = coeffs[k]

  def __getitem__(self, k):
    return self.__poly[k]

  def __setitem__(self, k, v):
    self.__poly[k] = v

  def __call__(self, x):
    val = 0
    for k in self.__poly:
      val += self.__poly[k]*(x**k)
    return val

  def __add__(self, other):
    new_poly = None
    if isinstance(other,Polynomial):
      new_poly = Polynomial(self.__poly)
      for k in other.__poly:
        new_poly[k] += other[k]
    elif isinstance(other,int) or isinstance(other,float):
      new_poly = Polynomial(self.__poly)
      new_poly[0] += other
    return new_poly


  def __sub__(self, other):
    new_poly = None
    if isinstance(other,Polynomial):
      new_poly = Polynomial(self.__poly)
      for k in other.__poly:
        new_poly[k] -= other[k]
    elif isinstance(other,int) or isinstance(other,float):
      new_poly = Polynomial(self.__poly)
      new_poly[0] -= other
    return new_poly

  def __mul__(self, other):
    new_poly = None
    if isinstance(other,Polynomial):
      new_poly = Polynomial([])
      for k1 in self.__poly:
        for k2 in other.__poly:
          new_poly[k1+k2] += self.__poly[k1] * other.__poly[k2] 
    elif isinstance(other,int) or isinstance(other,float):
      new_poly = Polynomial(self.__poly)
      for k in new_poly.__poly:
        new_poly[k] *= other
    return new_poly

  def __pow__(self, n):
    new_poly = Polynomial({0:1})
    for i in range(n):
      new_poly *= self
    return new_poly

  def derivative(self):
    new_poly = Polynomial({0:1})
    for k in self.__poly:
      if k > 0:
        new_poly[k-1] = k*self.__poly[k]
    return new_poly

  def __str__(self):
    str_poly = []
    for key in reversed(sorted(self.__poly.keys())):
      str_poly.append(f"{self[key]}X^{key}")
    return " + ".join(str_poly)

def newton_raphson(p, x, n_iter=20):
  d = p.derivative()
  for _ in range(n_iter):
    if d(x) ==0:
      break
    x -= p(x)/d(x)
  return x


if __name__ == "__main__":
  p = Polynomial({4: 2, 3: 5, 1: 6, 0: -2})
  q = Polynomial({3: 1, 2: 0.5, 1: -1, 0: 3})
  print(f"p = {p}")
  print(f"q = {q}")
  print(f"p+q = {p+q}")
  print(f"p*q = {p*q}")
  print(f"p^2 = {p**2}")
  print(f"p(3) = {p(3)}")
  print(f"(p+q)(20) = {(p+q)(20)}")
  print(f"p' = {p.derivative()}")
  x = newton_raphson(p, 5)
  print(f"p({x}) = {p(x)}")