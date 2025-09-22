from itertools import product
xs = [1,2,3,-99,97]

for i,j,k in product(xs,xs,xs):
    print(i,j,k)
