import timeit
from hcf import my_hcf, euclidian_hcf

# my algorithm
t1 = timeit.timeit(lambda: my_hcf(1234566, 654321), number=1000)

# Euclidean algorithm
t2 = timeit.timeit(lambda: euclidian_hcf(1234566, 654321), number=1000)

print(f"my: {t1}   euclid: {t2}")

print("-----------------------------------------------------------")