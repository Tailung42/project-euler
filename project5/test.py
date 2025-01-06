import timeit
from hcf import my_hcf, euclidian_hcf

# my algorithm
t1 = timeit.timeit(lambda: my_hcf(12345, 54321), number=100)

# Euclidean algorithm
t2 = timeit.timeit(lambda: euclidian_hcf(12345, 54321), number=100)

print(f"my: {t1}   euclid: {t2}")

