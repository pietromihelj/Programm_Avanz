from functools import reduce,partial

xs = [1,2,3,4,5,6,7,8,9]

print("numeri al quadrato",list(map(lambda x: x**2,xs)))
print("elementi pari",list(filter(lambda x: x%2 == 0,xs)))
print("somma",reduce(lambda x,y: x+y,xs))
print("prodotto",reduce(lambda x,y: x*y,xs))

map_squares = partial(map, lambda x: x**2) #sto fissando il primo parametro. in questo caso è una funzione
print(list(map_squares(xs)))

somma3 = partial(lambda x,y: x+y, 3)
print(somma3(100))