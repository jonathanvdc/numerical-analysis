from Polynomial import *
from math import sqrt

def fixpoint(f, x0, n):

    x = x_prev = x0
    for i in range(n):
        (x_prev, x) = (x, f(x))
        if x == x_prev:
            # Stop when we have obtained the correct result,
            # or when we hit the machine precision barrier.
            return i + 1, x

    return n, x

print(fixpoint(lambda x: sqrt(10 - x ** 3) / 2.0, 1.5, 20))
