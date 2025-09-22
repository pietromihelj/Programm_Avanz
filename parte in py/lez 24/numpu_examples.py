import numpy as np

a = np.array([1,2,3,4,5])
b = a.astype(float)
print(b.dtype, a.dtype)

rng = np.random.default_rng()

print(rng.integers(2,9,6,endpoint=True))
print(rng.random(6))
print(rng.normal(2,9,6).reshape(3,2))
print(np.any(a>4))
print(np.all(a>4))
print(np.where(a>=3))
print(np.clip(a,2,4))
print(a@b)