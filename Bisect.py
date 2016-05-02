from Polynomial import *

def bisect(poly, a0, b0, n):
    a = a0
    b = b0
    x = (a + b) / 2.0

    for i in range(n):
        x = (a + b) / 2.0

        fa = poly.get(a)
        fx = poly.get(x)

        if (fa * fx <= 0.0):
            b = x
        else:
            a = x

    return n, x

print(bisect(Polynomial([1, 4, 0, -10]), 1, 2, 20))
